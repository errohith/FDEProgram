import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent / "data" / "invoices.json"


def load_invoices() -> list[dict]:
    if not DATA_FILE.exists():
        return []
    with DATA_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_invoices(invoices_list: list[dict]) -> None:
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(invoices_list, file, indent=4)
