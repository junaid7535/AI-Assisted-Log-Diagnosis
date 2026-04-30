import re
from src.schemas.log_event import LogEvent


DEFAULT_PATTERN = re.compile(
    r"^(?P<timestamp>\S+\s+\S+)\s+"
    r"(?P<level>INFO|WARN|WARNING|ERROR|CRITICAL|DEBUG)\s+"
    r"(?:(?P<service>[\w.-]+)\s*-\s*)?"
    r"(?P<message>.*)$",
    re.IGNORECASE,
)


class LogParser:
    def __init__(self, pattern: re.Pattern | None = None):
        self.pattern = pattern or DEFAULT_PATTERN

    def parse_line(self, line: str, line_number: int) -> LogEvent:
        match = self.pattern.match(line)
        if not match:
            return LogEvent(line_number=line_number, raw=line, level="UNKNOWN", message=line)

        data = match.groupdict()
        return LogEvent(
            line_number=line_number,
            raw=line,
            timestamp=data.get("timestamp"),
            level=(data.get("level") or "UNKNOWN").upper(),
            service=data.get("service"),
            message=data.get("message") or line,
        )

    def parse_text(self, text: str) -> list[LogEvent]:
        lines = [line for line in text.splitlines() if line.strip()]
        return [self.parse_line(line, i + 1) for i, line in enumerate(lines)]
