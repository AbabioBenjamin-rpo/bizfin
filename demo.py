"""
demo.py — a quick tour of the bizfin library in action.
Run with: python demo.py
"""
from bizfin import loans, invoicing, profitability, depreciation, currency

print("=" * 50)
print("1. LOANS — EMI & Amortization")
print("=" * 50)
principal, rate, months = 10000, 18, 12
payment = loans.emi(principal, rate, months)
print(f"Loan: {currency.format_ghs(principal)} at {rate}% for {months} months")
print(f"Monthly EMI: {currency.format_ghs(payment)}")
print("\nFirst 3 months of amortization schedule:")
schedule = loans.amortization_schedule(principal, rate, months)
for row in schedule[:3]:
    print(f"  Month {row.month}: pay {row.payment}, "
          f"principal {row.principal_paid}, interest {row.interest_paid}, "
          f"balance left {row.remaining_balance}")

print("\n" + "=" * 50)
print("2. INVOICING — Ghana VAT/NHIL/GETFund")
print("=" * 50)
inv = invoicing.Invoice(customer_name="Kwame Stores")
inv.add_item("Bag of Rice", 2, 350.0)
inv.add_item("Cooking Oil (5L)", 3, 120.0)
print(inv.summary())

print("\n" + "=" * 50)
print("3. PROFITABILITY — Break-even & Margin")
print("=" * 50)
units = profitability.break_even_units(fixed_costs=5000, price_per_unit=50, variable_cost_per_unit=30)
print(f"Break-even point: {units} units")
margin = profitability.profit_margin(revenue=1000, cost=600)
print(f"Profit margin: {margin}%")
mk = profitability.markup(cost=100, selling_price=150)
print(f"Markup: {mk}%")

print("\n" + "=" * 50)
print("4. DEPRECIATION — Straight-line (5 years)")
print("=" * 50)
dep_schedule = depreciation.straight_line(cost=10000, salvage_value=1000, useful_life_years=5)
for row in dep_schedule:
    print(f"  Year {row.year}: expense {currency.format_ghs(row.depreciation_expense)}, "
          f"book value {currency.format_ghs(row.book_value)}")

print("\n" + "=" * 50)
print("5. CURRENCY — GHS formatting")
print("=" * 50)
print(currency.format_ghs(12450.5))
print(currency.format_ghs(12450.5, symbol=False))
print(currency.parse_ghs("GHS 12,450.50"))
