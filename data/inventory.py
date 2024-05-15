from dataclasses import dataclass
from database.database import Database
from data.utils import BaseManager

db = Database()


@dataclass
class Inventory:
    id: int
    name: str


class Inventories(BaseManager):
    @classmethod
    def search(cls, **kwargs):
        return BaseManager.search(**kwargs)


# inventories = Inventories()
# print(inventories.search(model_class=Inventory, table='inventory'))
