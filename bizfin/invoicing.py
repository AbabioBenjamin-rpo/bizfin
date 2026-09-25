"""
invoicing.py — build simple invoices with Ghana-style tax handling
(VAT + NHIL + GETFund, applied the way most Ghanaian retail invoices do:
each levy calculated on the base price and summed, not compounded).
"""
from dataclasses import dataclass, field
from typing import List


# Standard Ghana rates as of common practice (adjustable by the caller).
DEFAULT_VAT_RATE = 15.0
DEFAULT_NHIL_RATE = 2.5
DEFAULT_GETFUND_RATE = 2.5


@dataclass
class LineItem:
    description: str
    quantity: float
    unit_price: float

    @property
    def subtotal(self) -> float:
        return round(self.quantity * self.unit_price, 2)


@dataclass
class Invoice:
    customer_name: str
    items: List[LineItem] = field(default_factory=list)
    discount_percent: float = 0.0
    vat_rate: float = DEFAULT_VAT_RATE
    nhil_rate: float = DEFAULT_NHIL_RATE
    getfund_rate: float = DEFAULT_GETFUND_RATE

    def add_item(self, description: str, quantity: float, unit_price: float) -> None:
        """Add a line item to the invoice."""
        self.items.append(LineItem(description, quantity, unit_price))

    @property
    def gross_subtotal(self) -> float:
        return round(sum(item.subtotal for item in self.items), 2)

    @property
    def discount_amount(self) -> float:
        return round(self.gross_subtotal * (self.discount_percent / 100), 2)

    @property
    def taxable_amount(self) -> float:
        return round(self.gross_subtotal - self.discount_amount, 2)

    @property
    def vat_amount(self) -> float:
        return round(self.taxable_amount * (self.vat_rate / 100), 2)

    @property
    def nhil_amount(self) -> float:
        return round(self.taxable_amount * (self.nhil_rate / 100), 2)

    @property
    def getfund_amount(self) -> float:
        return round(self.taxable_amount * (self.getfund_rate / 100), 2)

    @property
    def total_tax(self) -> float:
        return round(self.vat_amount + self.nhil_amount + self.getfund_amount, 2)

    @property
    def grand_total(self) -> float:
        return round(self.taxable_amount + self.total_tax, 2)

    def summary(self) -> str:
        """Return a human-readable breakdown of the invoice."""
        lines = [f"Invoice for {self.customer_name}", "-" * 40]
        for item in self.items:
            lines.append(
                f"{item.description:<20} {item.quantity:>6} x {item.unit_price:>8.2f} = {item.subtotal:>10.2f}"
            )
        lines.append("-" * 40)
        lines.append(f"{'Subtotal':<20} {self.gross_subtotal:>10.2f}")
        if self.discount_percent:
            lines.append(f"{'Discount (' + str(self.discount_percent) + '%)':<20} -{self.discount_amount:>9.2f}")
        lines.append(f"{'VAT (' + str(self.vat_rate) + '%)':<20} {self.vat_amount:>10.2f}")
        lines.append(f"{'NHIL (' + str(self.nhil_rate) + '%)':<20} {self.nhil_amount:>10.2f}")
        lines.append(f"{'GETFund (' + str(self.getfund_rate) + '%)':<20} {self.getfund_amount:>10.2f}")
        lines.append(f"{'TOTAL':<20} {self.grand_total:>10.2f}")
        return "\n".join(lines)
