# AI-Assisted Log Diagnosis & Root-Cause Detection

AI-Assisted Log Diagnosis for automated log parsing, anomaly detection, clustering, and root-cause analysis reports.

## Features

- Log ingestion from `.log`, `.txt`, `.jsonl`, `.csv`
- Regex-based log parsing
- TF-IDF feature extraction
- Isolation Forest anomaly detection
- DBSCAN log clustering
- Rule-based RCA suggestions
- Optional LLM RCA report interface
- FastAPI backend
- CLI scripts
- Docker support
- Unit tests

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements/base.txt
python scripts/run_demo.py
```

## Run API

```bash
uvicorn src.api.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

## Example CLI

```bash
python scripts/analyze_logs.py --input data/samples/system.log
```

## Project Structure

```text
src/ingestion      Read logs from files
src/parsing        Convert raw logs into structured events
src/features       Generate ML features
src/anomaly        Detect unusual log lines/sequences
src/clustering     Group similar logs
src/diagnosis      Root cause scoring and explanation
src/llm            Optional report generator
src/api            FastAPI app
src/evaluation     Metrics and dataset evaluation
```
