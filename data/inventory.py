from dataclasses import dataclass
from database.database import Database
from data.utils import Searchable

db = Database()


@dataclass
class Inventory:
    id: int
    name: str


class Inventories(Searchable):
    child = Inventory


print(Inventories().search())
