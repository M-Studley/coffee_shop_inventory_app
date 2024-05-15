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
    @classmethod
    def search(cls, **kwargs):
        return BaseManager.search(**kwargs)


# item_infos = ItemInfos()
# print(item_infos.search(model_class=ItemInfo, table='item_info'))
