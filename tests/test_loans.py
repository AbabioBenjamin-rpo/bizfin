import pytest
from bizfin import loans


def test_simple_interest():
    assert loans.simple_interest(1000, 10, 2) == 200


def test_compound_interest():
    result = loans.compound_interest(1000, 10, 1, compounds_per_year=1)
    assert round(result, 2) == 100.0


def test_emi_zero_rate():
    assert loans.emi(1200, 0, 12) == 100.0


def test_emi_positive_rate():
    result = loans.emi(10000, 12, 12)
    assert result > 0


def test_amortization_schedule_length():
    schedule = loans.amortization_schedule(5000, 15, 6)
    assert len(schedule) == 6
    assert schedule[-1].remaining_balance == 0.0


def test_negative_principal_raises():
    with pytest.raises(ValueError):
        loans.simple_interest(-100, 10, 1)
