from sklearn.ensemble import IsolationForest
from src.schemas.log_event import LogEvent


class AnomalyDetector:
    def __init__(self, contamination: float = 0.12, random_state: int = 42):
        self.model = IsolationForest(contamination=contamination, random_state=random_state)

    def fit_predict(self, features, events: list[LogEvent]) -> list[LogEvent]:
        labels = self.model.fit_predict(features)
        scores = self.model.decision_function(features)
        for event, label, score in zip(events, labels, scores):
            event.is_anomaly = label == -1 or event.level in {"ERROR", "CRITICAL"}
            event.anomaly_score = float(score)
        return events
