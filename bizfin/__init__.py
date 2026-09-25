"""
bizfin — a lightweight Python toolkit for common business & finance calculations.

Modules:
    loans        Simple/compound interest, EMI, amortization schedules
    invoicing    Invoice line items, VAT/NHIL-style tax handling, totals
    profitability Break-even point, profit margin, markup
    depreciation Straight-line and reducing-balance depreciation
    currency     GHS (Ghana Cedi) currency formatting
"""

from . import loans
from . import invoicing
from . import profitability
from . import depreciation
from . import currency

__version__ = "0.1.0"
__all__ = [
    "loans",
    "invoicing",
    "profitability",
    "depreciation",
    "currency",
]
