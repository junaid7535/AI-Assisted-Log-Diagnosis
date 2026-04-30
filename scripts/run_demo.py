from pathlib import Path
from rich import print
from src.api.pipeline import LogRCAPipeline

sample = Path("data/samples/system.log").read_text(encoding="utf-8")
result = LogRCAPipeline().run(sample)
print(result.model_dump_json(indent=2))
