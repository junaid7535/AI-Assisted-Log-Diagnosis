from src.parsing.log_parser import LogParser
from src.features.vectorizer import LogFeatureExtractor
from src.anomaly.detector import AnomalyDetector
from src.clustering.log_clusterer import LogClusterer
from src.diagnosis.root_cause import RootCauseAnalyzer
from src.llm.report_generator import RCAReportGenerator
from src.schemas.log_event import AnalysisResponse


class LogRCAPipeline:
    def __init__(self):
        self.parser = LogParser()
        self.features = LogFeatureExtractor()
        self.detector = AnomalyDetector()
        self.clusterer = LogClusterer()
        self.rca = RootCauseAnalyzer()
        self.reporter = RCAReportGenerator()

    def run(self, raw_logs: str) -> AnalysisResponse:
        events = self.parser.parse_text(raw_logs)
        if not events:
            return AnalysisResponse(total_events=0, anomalies=[], findings=[], summary="No logs provided.")

        matrix = self.features.fit_transform(events)
        events = self.detector.fit_predict(matrix, events)
        events = self.clusterer.fit_predict(matrix, events)
        findings = self.rca.analyze(events)
        summary = self.reporter.generate(events, findings)
        anomalies = [e for e in events if e.is_anomaly]

        return AnalysisResponse(
            total_events=len(events),
            anomalies=anomalies,
            findings=findings,
            summary=summary,
        )
