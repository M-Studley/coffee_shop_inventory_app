from dataclasses import dataclass
from database.database import Database
from data.utils import Searchable

db = Database()


@dataclass
class ItemInfo:
    id: int
    _item_id: int
    price: float
    purchase_date: str
    check_in: str
    check_out: str
    order_status: str


class ItemInfos(Searchable):
    child = ItemInfo
