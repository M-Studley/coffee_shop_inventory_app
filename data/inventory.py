from dataclasses import dataclass
from database.database import Database
from data.utils import BaseManager

db = Database()


@dataclass
class Inventory:
    id: int
    name: str


class Inventories(BaseManager):
    def __init__(self):
        super().__init__('inventory', Inventory)


# print(Inventories().full_list)
# print(Inventories().search(id=1))

# class Inventories:
#     @cached_property
#     def full_list(self) -> list[Inventory]:
#         query = "SELECT * FROM `inventory`"
#         all_rows = db.fetchall(query)
#         return [Inventory(**row) for row in all_rows]
#
#     @cache
#     def search(self, **kwargs) -> list[Inventory] | list[str]:
#         results = self.full_list[:]
#         for inventory in self.full_list:
#             for key in kwargs:
#                 try:
#                     value = getattr(inventory, key)
#                 except AttributeError:
#                     return [f"Key '{key}' does not exist..."]
#
#                 if value != kwargs[key]:
#                     results.remove(inventory)
#                     break
#
#         return results
