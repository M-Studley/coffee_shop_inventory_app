from dataclasses import dataclass
from database.database import Database
from data.utils import BaseManager

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


class ItemInfos(BaseManager):
    def __init__(self):
        super().__init__('item_info', ItemInfo)


item_infos = ItemInfos()
print(item_infos.full_list())
print(item_infos.search(id=1))
