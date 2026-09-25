"""
profitability.py — break-even analysis, profit margin, and markup calculations.
"""


def break_even_units(fixed_costs: float, price_per_unit: float, variable_cost_per_unit: float) -> float:
    """
    Calculate the break-even point in units.

    Args:
        fixed_costs: Total fixed costs (rent, salaries, etc.)
        price_per_unit: Selling price per unit
        variable_cost_per_unit: Variable cost per unit (materials, etc.)

    Returns:
        The number of units that must be sold to cover all costs.
    """
    contribution_margin = price_per_unit - variable_cost_per_unit
    if contribution_margin <= 0:
        raise ValueError("price_per_unit must exceed variable_cost_per_unit")
    return fixed_costs / contribution_margin


def break_even_revenue(fixed_costs: float, price_per_unit: float, variable_cost_per_unit: float) -> float:
    """Calculate the break-even point in revenue (GHS)."""
    units = break_even_units(fixed_costs, price_per_unit, variable_cost_per_unit)
    return round(units * price_per_unit, 2)


def profit_margin(revenue: float, cost: float) -> float:
    """
    Calculate profit margin as a percentage of revenue.

    Args:
        revenue: Total sales revenue
        cost: Total cost of goods sold

    Returns:
        Profit margin percentage.
    """
    if revenue <= 0:
        raise ValueError("revenue must be positive")
    return round(((revenue - cost) / revenue) * 100, 2)


def markup(cost: float, selling_price: float) -> float:
    """
    Calculate markup as a percentage of cost.

    Args:
        cost: Cost price of the item
        selling_price: Selling price of the item

    Returns:
        Markup percentage.
    """
    if cost <= 0:
        raise ValueError("cost must be positive")
    return round(((selling_price - cost) / cost) * 100, 2)


def price_from_markup(cost: float, markup_percent: float) -> float:
    """Given a cost and desired markup percentage, return the selling price."""
    if cost < 0 or markup_percent < 0:
        raise ValueError("cost and markup_percent must be non-negative")
    return round(cost * (1 + markup_percent / 100), 2)
