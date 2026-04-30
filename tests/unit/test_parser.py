from src.parsing.log_parser import LogParser


def test_parse_line():
    event = LogParser().parse_line("2026-04-30 10:03:45 ERROR api - database timeout", 1)
    assert event.level == "ERROR"
    assert "database" in event.message
