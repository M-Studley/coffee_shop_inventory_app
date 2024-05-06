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


print(ItemInfos().full_list)
print(ItemInfos().search(id=1))


# class ItemInfos:
#     @cached_property
#     def full_list(self) -> list[ItemInfo]:
#         query = "SELECT * FROM `item_info`"
#         all_rows = db.fetchall(query)
#         return [ItemInfo(**row) for row in all_rows]
#
#     @cache
#     def search(self, **kwargs) -> list[ItemInfo] | list[str]:
#         results = self.full_list[:]
#         for item_info in self.full_list:
#             for key in kwargs:
#                 try:
#                     value = getattr(item_info, key)
#                 except AttributeError:
#                     return [f"Key '{key}' does not exist..."]
#
#                 if value != kwargs[key]:
#                     results.remove(item_info)
#                     break
#
#         return results
