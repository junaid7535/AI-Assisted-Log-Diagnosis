from collections import Counter
from src.schemas.log_event import LogEvent, RCAFinding
from src.diagnosis.rules import ROOT_CAUSE_RULES


class RootCauseAnalyzer:
    def analyze(self, events: list[LogEvent]) -> list[RCAFinding]:
        suspicious = [e for e in events if e.is_anomaly or e.level in {"ERROR", "CRITICAL", "WARN", "WARNING"}]
        if not suspicious:
            return [RCAFinding(
                suspected_root_cause="No obvious failure pattern detected",
                confidence=0.35,
                evidence=[],
                recommendation="Collect more logs around the incident window and include metrics/traces.",
            )]

        findings: list[RCAFinding] = []
        messages = [e.raw.lower() for e in suspicious]

        for rule in ROOT_CAUSE_RULES:
            evidence = [e.raw for e in suspicious if any(k in e.raw.lower() for k in rule["keywords"])]
            if evidence:
                confidence = min(0.95, 0.45 + len(evidence) / max(len(suspicious), 1))
                findings.append(RCAFinding(
                    suspected_root_cause=rule["name"],
                    confidence=round(confidence, 2),
                    evidence=evidence[:5],
                    recommendation=rule["recommendation"],
                ))

        if not findings:
            common_terms = Counter(" ".join(messages).split()).most_common(5)
            findings.append(RCAFinding(
                suspected_root_cause="Unknown anomaly pattern",
                confidence=0.45,
                evidence=[e.raw for e in suspicious[:5]],
                recommendation=f"Review repeated terms: {common_terms}. Add domain-specific RCA rules or labels.",
            ))

        return sorted(findings, key=lambda f: f.confidence, reverse=True)
