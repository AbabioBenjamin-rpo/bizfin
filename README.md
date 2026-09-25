# bizfin

A lightweight Python toolkit for common **business & finance calculations**, built for small businesses, students, and anyone who needs quick, reliable finance math without a spreadsheet.

## Features

- **Loans** — simple interest, compound interest, EMI, and full amortization schedules
- **Invoicing** — line-item invoices with Ghana-style VAT / NHIL / GETFund tax handling and discounts
- **Profitability** — break-even point (units & revenue), profit margin, markup
- **Depreciation** — straight-line and reducing-balance depreciation schedules
- **Currency** — format and parse amounts as Ghana Cedi (GHS)

## Installation

```bash
pip install .
```

Or, for development:

```bash
pip install -e .
pip install pytest  # to run tests
```

## Quick start

```python
from bizfin import loans, invoicing, profitability, depreciation, currency

# Loan EMI
monthly_payment = loans.emi(principal=10000, annual_rate=18, months=12)
print(currency.format_ghs(monthly_payment))  # e.g. GHS 916.67

# Amortization schedule
schedule = loans.amortization_schedule(10000, 18, 12)
for row in schedule[:3]:
    print(row)

# Invoice with Ghana tax handling
inv = invoicing.Invoice(customer_name="Kwame Stores")
inv.add_item("Bag of Rice", 2, 350.0)
inv.add_item("Cooking Oil (5L)", 3, 120.0)
print(inv.summary())
print(currency.format_ghs(inv.grand_total))

# Break-even analysis
units = profitability.break_even_units(fixed_costs=5000, price_per_unit=50, variable_cost_per_unit=30)
print(f"Break-even at {units} units")

# Depreciation
schedule = depreciation.straight_line(cost=10000, salvage_value=1000, useful_life_years=5)
for row in schedule:
    print(row)
```

## Running tests

```bash
pytest
```

## Project structure

```
bizfin/
├── bizfin/
│   ├── __init__.py
│   ├── loans.py
│   ├── invoicing.py
│   ├── profitability.py
│   ├── depreciation.py
│   └── currency.py
├── tests/
│   ├── test_loans.py
│   ├── test_invoicing.py
│   ├── test_profitability.py
│   ├── test_depreciation.py
│   └── test_currency.py
├── pyproject.toml
├── README.md
└── LICENSE
```

## Author

Ababio Benjamin Kofi (Benji) — BSc. Business Administration (Business Information Technology), KNUST School of Business.

## License

MIT
