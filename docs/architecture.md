# Architecture

1. Ingestion reads raw log files.
2. Parser converts each line to a structured `LogEvent`.
3. Feature extractor builds TF-IDF + numeric severity features.
4. Isolation Forest flags anomalous log events.
5. DBSCAN clusters similar logs.
6. RCA rules score likely root causes.
7. Report generator creates a human-readable summary.
