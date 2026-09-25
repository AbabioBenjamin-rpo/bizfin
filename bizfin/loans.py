"""
loans.py — interest and loan repayment calculations.
"""
from dataclasses import dataclass
from typing import List


def simple_interest(principal: float, rate: float, time_years: float) -> float:
    """
    Calculate simple interest.

    Args:
        principal: Initial amount (e.g. GHS 5000)
        rate: Annual interest rate as a percentage (e.g. 12 for 12%)
        time_years: Duration of the loan/investment in years

    Returns:
        The interest earned/owed (not including principal).
    """
    if principal < 0 or rate < 0 or time_years < 0:
        raise ValueError("principal, rate and time_years must be non-negative")
    return principal * (rate / 100) * time_years


def compound_interest(
    principal: float,
    rate: float,
    time_years: float,
    compounds_per_year: int = 1,
) -> float:
    """
    Calculate compound interest.

    Args:
        principal: Initial amount
        rate: Annual interest rate as a percentage
        time_years: Duration in years
        compounds_per_year: Number of times interest compounds per year
            (1 = annually, 12 = monthly, 4 = quarterly)

    Returns:
        The total interest earned/owed (final amount minus principal).
    """
    if principal < 0 or rate < 0 or time_years < 0 or compounds_per_year <= 0:
        raise ValueError("invalid arguments to compound_interest")
    amount = principal * (1 + (rate / 100) / compounds_per_year) ** (
        compounds_per_year * time_years
    )
    return amount - principal


def emi(principal: float, annual_rate: float, months: int) -> float:
    """
    Calculate the Equated Monthly Installment (EMI) for a loan.

    Args:
        principal: Loan amount
        annual_rate: Annual interest rate as a percentage (e.g. 18 for 18%)
        months: Loan tenure in months

    Returns:
        The fixed monthly repayment amount.
    """
    if principal <= 0 or months <= 0:
        raise ValueError("principal and months must be positive")
    if annual_rate == 0:
        return principal / months

    monthly_rate = (annual_rate / 100) / 12
    factor = (1 + monthly_rate) ** months
    return principal * monthly_rate * factor / (factor - 1)


@dataclass
class AmortizationRow:
    month: int
    payment: float
    principal_paid: float
    interest_paid: float
    remaining_balance: float


def amortization_schedule(
    principal: float, annual_rate: float, months: int
) -> List[AmortizationRow]:
    """
    Build a full month-by-month amortization schedule for a loan.

    Args:
        principal: Loan amount
        annual_rate: Annual interest rate as a percentage
        months: Loan tenure in months

    Returns:
        A list of AmortizationRow entries, one per month, showing how
        each payment splits between interest and principal.
    """
    monthly_payment = emi(principal, annual_rate, months)
    monthly_rate = (annual_rate / 100) / 12
    balance = principal
    schedule = []

    for m in range(1, months + 1):
        interest_paid = balance * monthly_rate
        principal_paid = monthly_payment - interest_paid
        balance = max(0.0, balance - principal_paid)
        schedule.append(
            AmortizationRow(
                month=m,
                payment=round(monthly_payment, 2),
                principal_paid=round(principal_paid, 2),
                interest_paid=round(interest_paid, 2),
                remaining_balance=round(balance, 2),
            )
        )
    return schedule
