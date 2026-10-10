from typing import Any


def get_invoice_value(invoice: dict, key: str, default: Any = "") -> Any:
    """Read an invoice field with dict.get so missing values have a default."""
    return invoice.get(key, default)
