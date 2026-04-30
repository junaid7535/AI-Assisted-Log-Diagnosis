from pathlib import Path
import json
import pandas as pd


class LogLoader:
    def load_text(self, path: str | Path) -> str:
        return Path(path).read_text(encoding="utf-8", errors="ignore")

    def load_lines(self, path: str | Path) -> list[str]:
        return [line.rstrip("\n") for line in self.load_text(path).splitlines() if line.strip()]

    def load_jsonl(self, path: str | Path) -> list[dict]:
        records = []
        with Path(path).open("r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    records.append(json.loads(line))
        return records

    def load_csv(self, path: str | Path) -> pd.DataFrame:
        return pd.read_csv(path)
