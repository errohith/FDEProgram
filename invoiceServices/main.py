from .Helpers import load_invoice_data
from .dec_get import get_invoice_value
from .enumerate import numbered
from .grouping import duplicate_invoices, totals_by_vendor
from .sorting import sort_invoices_by_vendor


def main() -> None:
    invoices = load_invoice_data()
    sorted_invoices = sort_invoices_by_vendor(invoices)

    print("Exercise 1: Total invoice amount by vendor")
    for vendor, total in sorted(totals_by_vendor(invoices).items()):
        print(f"{vendor}: {total:,.2f}")

    print("\nExercise 2: Duplicate vendor invoices")
    duplicates = duplicate_invoices(sorted_invoices)
    if not duplicates:
        print("No duplicate vendors found.")
        return

    for position, invoice in numbered(duplicates):
        print(
            f"{position}. "
            f"Invoice {get_invoice_value(invoice, 'invoice_id', '<unknown>')} | "
            f"Vendor: {get_invoice_value(invoice, 'vendor')} | "
            f"Amount: {float(get_invoice_value(invoice, 'amount')):,.2f}"
        )


if __name__ == "__main__":
    main()
