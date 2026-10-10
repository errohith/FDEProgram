from collections.abc import Iterable, Iterator
from typing import Any


def numbered(items: Iterable[Any]) -> Iterator[tuple[int, Any]]:
    """Return items paired with a one-based position."""
    return enumerate(items, start=1)
