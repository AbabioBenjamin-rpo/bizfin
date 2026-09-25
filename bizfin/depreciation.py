"""
depreciation.py — straight-line and reducing-balance depreciation schedules.
"""
from dataclasses import dataclass
from typing import List


@dataclass
class DepreciationRow:
    year: int
    depreciation_expense: float
    accumulated_depreciation: float
    book_value: float


def straight_line(cost: float, salvage_value: float, useful_life_years: int) -> List[DepreciationRow]:
    """
    Calculate a straight-line depreciation schedule.

    Args:
        cost: Original cost of the asset
        salvage_value: Estimated residual value at end of useful life
        useful_life_years: Useful life of the asset in years

    Returns:
        A list of DepreciationRow entries, one per year.
    """
    if useful_life_years <= 0:
        raise ValueError("useful_life_years must be positive")
    if salvage_value > cost:
        raise ValueError("salvage_value cannot exceed cost")

    annual_expense = round((cost - salvage_value) / useful_life_years, 2)
    schedule = []
    accumulated = 0.0

    for year in range(1, useful_life_years + 1):
        accumulated = round(accumulated + annual_expense, 2)
        book_value = round(cost - accumulated, 2)
        schedule.append(DepreciationRow(year, annual_expense, accumulated, book_value))
    return schedule


def reducing_balance(cost: float, rate: float, useful_life_years: int) -> List[DepreciationRow]:
    """
    Calculate a reducing (declining) balance depreciation schedule.

    Args:
        cost: Original cost of the asset
        rate: Annual depreciation rate as a percentage (e.g. 20 for 20%)
        useful_life_years: Number of years to project

    Returns:
        A list of DepreciationRow entries, one per year.
    """
    if useful_life_years <= 0 or rate <= 0:
        raise ValueError("useful_life_years and rate must be positive")

    schedule = []
    book_value = cost
    accumulated = 0.0

    for year in range(1, useful_life_years + 1):
        expense = round(book_value * (rate / 100), 2)
        accumulated = round(accumulated + expense, 2)
        book_value = round(book_value - expense, 2)
        schedule.append(DepreciationRow(year, expense, accumulated, book_value))
    return schedule
