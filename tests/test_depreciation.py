from bizfin import depreciation as dep


def test_straight_line():
    schedule = dep.straight_line(10000, 1000, 3)
    assert len(schedule) == 3
    assert schedule[0].depreciation_expense == 3000.0
    assert schedule[-1].book_value == 1000.0


def test_reducing_balance():
    schedule = dep.reducing_balance(10000, 20, 3)
    assert len(schedule) == 3
    assert schedule[0].depreciation_expense == 2000.0
    assert schedule[0].book_value == 8000.0
    assert schedule[1].depreciation_expense == 1600.0
