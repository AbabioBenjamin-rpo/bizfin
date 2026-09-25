from bizfin.invoicing import Invoice


def test_invoice_totals():
    inv = Invoice(customer_name="Kwame Stores")
    inv.add_item("Bag of Rice", 2, 350.0)
    inv.add_item("Cooking Oil (5L)", 3, 120.0)

    assert inv.gross_subtotal == 1060.0
    assert inv.vat_amount == round(1060.0 * 0.15, 2)
    assert inv.grand_total > inv.gross_subtotal


def test_invoice_with_discount():
    inv = Invoice(customer_name="Ama Traders", discount_percent=10)
    inv.add_item("Item A", 1, 100.0)
    assert inv.discount_amount == 10.0
    assert inv.taxable_amount == 90.0
