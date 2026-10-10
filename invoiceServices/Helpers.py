from .utils import load_invoices


def load_invoice_data() -> list[dict]:
    """Load the invoice records used by the exercises."""
    invoices = load_invoices()
    if not isinstance(invoices, list):
        raise ValueError("Invoice data must be a JSON list.")
    return invoices
