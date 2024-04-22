from dataclasses import dataclass


@dataclass
class ItemInfo:
    id: int
    price: float
    purchase_date: str
    checked_in: str
    checked_out: str
    order_status: str
