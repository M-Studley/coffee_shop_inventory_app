from dataclasses import dataclass


@dataclass
class Item:
    id: int
    name: str
    measurement_amount: int
    measurement_type: list
    sku: str
