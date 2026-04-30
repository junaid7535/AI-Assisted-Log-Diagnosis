import argparse
from pathlib import Path
from rich import print
from src.api.pipeline import LogRCAPipeline


def main():
    parser = argparse.ArgumentParser(description="Analyze logs and generate RCA findings")
    parser.add_argument("--input", required=True, help="Path to log file")
    args = parser.parse_args()

    text = Path(args.input).read_text(encoding="utf-8", errors="ignore")
    result = LogRCAPipeline().run(text)

    print("[bold green]Summary[/bold green]")
    print(result.summary)
    print("\n[bold yellow]Findings[/bold yellow]")
    for finding in result.findings:
        print(f"- {finding.suspected_root_cause} | confidence={finding.confidence}")
        print(f"  recommendation: {finding.recommendation}")


if __name__ == "__main__":
    main()
