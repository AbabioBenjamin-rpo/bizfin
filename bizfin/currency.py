"""
currency.py — format amounts as Ghana Cedi (GHS).
"""


def format_ghs(amount: float, symbol: bool = True) -> str:
    """
    Format a number as a Ghana Cedi amount with thousands separators.

    Args:
        amount: The numeric amount to format
        symbol: Whether to prefix the currency symbol "GHS " (default True)

    Returns:
        A formatted string, e.g. "GHS 12,450.50"

    Examples:
        >>> format_ghs(12450.5)
        'GHS 12,450.50'
        >>> format_ghs(12450.5, symbol=False)
        '12,450.50'
    """
    formatted = f"{amount:,.2f}"
    return f"GHS {formatted}" if symbol else formatted


def parse_ghs(text: str) -> float:
    """
    Parse a GHS-formatted string back into a float.

    Args:
        text: A string like "GHS 12,450.50" or "12,450.50"

    Returns:
        The numeric value as a float.
    """
    cleaned = text.replace("GHS", "").replace(",", "").strip()
    return float(cleaned)
