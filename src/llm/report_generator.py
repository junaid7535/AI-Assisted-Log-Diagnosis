from src.schemas.log_event import LogEvent, RCAFinding


class RCAReportGenerator:
    def generate(self, events: list[LogEvent], findings: list[RCAFinding]) -> str:
        anomaly_count = sum(e.is_anomaly for e in events)
        top = findings[0] if findings else None
        if not top:
            return "No RCA finding was generated."
        return (
            f"Analyzed {len(events)} log events and detected {anomaly_count} anomalies. "
            f"Most likely root cause: {top.suspected_root_cause} "
            f"with confidence {top.confidence}. Recommended action: {top.recommendation}"
        )
