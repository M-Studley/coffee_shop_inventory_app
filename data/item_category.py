from dataclasses import dataclass
from database.database import Database
from data.utils import Searchable

db = Database()


@dataclass
class ItemCategory:
    id: int
    name: str
    description: str
    
    
class ItemCategories(Searchable):
    child = ItemCategory


# print(ItemCategories().search())
