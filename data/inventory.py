from dataclasses import dataclass
from database.database import Database
from data.item import Items
from data.utils import Searchable

db = Database()


@dataclass
class Inventory:
    id: int
    name: str
    _store_id: int

    @property
    def items(self):
        return Items().search(_inventory_id=self.id)


class Inventories(Searchable):
    child = Inventory
