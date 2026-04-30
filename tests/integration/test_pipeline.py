from src.api.pipeline import LogRCAPipeline


def test_pipeline_runs():
    logs = "2026-04-30 10:03:45 ERROR api - database connection timeout"
    result = LogRCAPipeline().run(logs)
    assert result.total_events == 1
    assert result.findings
