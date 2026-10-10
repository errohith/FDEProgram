from collections import defaultdict
from collections.abc import Iterable

from .dec_get import get_invoice_value


def _vendor_key(invoice: dict) -> str:
    return str(get_invoice_value(invoice, "vendor")).strip().casefold()


def totals_by_vendor(invoices: Iterable[dict]) -> dict[str, float]:
    """Sum invoice amounts for each vendor, ignoring case and outer spaces."""
    totals: dict[str, float] = {}
    vendor_names: dict[str, str] = {}

    for invoice in invoices:
        key = _vendor_key(invoice)
        if not key:
            raise ValueError("Every invoice must have a vendor.")
        vendor_names.setdefault(key, str(get_invoice_value(invoice, "vendor")).strip())

        try:
            amount = float(get_invoice_value(invoice, "amount"))
        except (TypeError, ValueError) as error:
            raise ValueError(
                f"Invoice {get_invoice_value(invoice, 'invoice_id', '<unknown>')} "
                "has an invalid amount."
            ) from error
        totals[key] = totals.get(key, 0.0) + amount

    return {vendor_names[key]: total for key, total in totals.items()}


def duplicate_invoices(invoices: Iterable[dict]) -> list[dict]:
    """Return every invoice belonging to a vendor with multiple invoices."""
    invoices_list = list(invoices)
    counts: dict[str, int] = defaultdict(int)
    for invoice in invoices_list:
        key = _vendor_key(invoice)
        if not key:
            raise ValueError("Every invoice must have a vendor.")
        counts[key] += 1

    return [invoice for invoice in invoices_list if counts[_vendor_key(invoice)] > 1]
