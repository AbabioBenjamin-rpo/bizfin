from bizfin import currency


def test_format_ghs_with_symbol():
    assert currency.format_ghs(12450.5) == "GHS 12,450.50"


def test_format_ghs_without_symbol():
    assert currency.format_ghs(12450.5, symbol=False) == "12,450.50"


def test_parse_ghs():
    assert currency.parse_ghs("GHS 12,450.50") == 12450.50


def test_parse_ghs_no_symbol():
    assert currency.parse_ghs("12,450.50") == 12450.50
