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


# inventories = Inventories()
# print(inventories.full_list())
# print()
# print(inventories.search(id=1))
