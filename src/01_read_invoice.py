import csv
import math
from pathlib import Path


DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "homework_invoices.csv"


def main() -> None:
    total_invoices = 0
    high_amount_invoices = 0
    invalid_amount_invoices = 0

    with DATA_FILE.open(mode="r", newline="", encoding="utf-8") as file:
        csv_reader = csv.DictReader(file)
        for invoice in csv_reader:
            total_invoices += 1
            vendor = (invoice.get("vendor") or "").strip()
            raw_amount = (invoice.get("amount") or "").strip()
            status = (invoice.get("status") or "").strip()

            try:
                if not raw_amount:
                    raise ValueError("missing amount")
                amount = float(raw_amount)
                if not math.isfinite(amount):
                    raise ValueError("amount is not a finite number")
            except ValueError:
                invalid_amount_invoices += 1
                print(
                    f"Vendor: {vendor}, Amount: {raw_amount or 'missing'}, "
                    f"Status: {status} - invalid amount"
                )
                continue

            print(f"Vendor: {vendor}, Amount: {amount}, Status: {status}")
            if amount > 100_000:
                high_amount_invoices += 1

    print("\nInvoice Summary")
    print(f"Total invoices read: {total_invoices}")
    print(f"Invoices with amount greater than 100,000: {high_amount_invoices}")
    print(f"Invoices with missing/invalid amount: {invalid_amount_invoices}")


if __name__ == "__main__":
    main()
