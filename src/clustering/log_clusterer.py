from sklearn.cluster import DBSCAN
from src.schemas.log_event import LogEvent


class LogClusterer:
    def __init__(self, eps: float = 0.45, min_samples: int = 2):
        self.model = DBSCAN(eps=eps, min_samples=min_samples, metric="cosine")

    def fit_predict(self, features, events: list[LogEvent]) -> list[LogEvent]:
        labels = self.model.fit_predict(features)
        for event, label in zip(events, labels):
            event.cluster_id = int(label)
        return events
