from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import hstack
import numpy as np
from src.schemas.log_event import LogEvent


class LogFeatureExtractor:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(max_features=3000, ngram_range=(1, 2), stop_words="english")

    def _numeric_features(self, events: list[LogEvent]):
        severity = {"DEBUG": 0, "INFO": 1, "WARN": 2, "WARNING": 2, "ERROR": 3, "CRITICAL": 4, "UNKNOWN": 1}
        return np.array([[severity.get(e.level, 1), len(e.message)] for e in events])

    def fit_transform(self, events: list[LogEvent]):
        texts = [f"{e.level} {e.service or ''} {e.message}" for e in events]
        text_features = self.vectorizer.fit_transform(texts)
        return hstack([text_features, self._numeric_features(events)])

    def transform(self, events: list[LogEvent]):
        texts = [f"{e.level} {e.service or ''} {e.message}" for e in events]
        text_features = self.vectorizer.transform(texts)
        return hstack([text_features, self._numeric_features(events)])
