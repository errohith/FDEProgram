from collections.abc import Iterable

from .dec_get import get_invoice_value


def sort_invoices_by_vendor(invoices: Iterable[dict]) -> list[dict]:
    """Sort invoices by vendor and then invoice ID."""
    return sorted(
        invoices,
        key=lambda invoice: (
            str(get_invoice_value(invoice, "vendor")).strip().casefold(),
            str(get_invoice_value(invoice, "invoice_id")).strip().casefold(),
        ),
    )
