import pytest
from bizfin import profitability as pf


def test_break_even_units():
    assert pf.break_even_units(1000, 50, 30) == 50


def test_break_even_revenue():
    assert pf.break_even_revenue(1000, 50, 30) == 2500.0


def test_profit_margin():
    assert pf.profit_margin(1000, 600) == 40.0


def test_markup():
    assert pf.markup(100, 150) == 50.0


def test_price_from_markup():
    assert pf.price_from_markup(100, 50) == 150.0


def test_invalid_contribution_margin():
    with pytest.raises(ValueError):
        pf.break_even_units(1000, 20, 30)
