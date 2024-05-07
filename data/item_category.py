from dataclasses import dataclass
from database.database import Database
from data.utils import BaseManager

db = Database()


@dataclass
class ItemCategory:
    id: int
    name: str
    description: str
    
    
class ItemCategories(BaseManager):
    def __init__(self):
        super().__init__('item_category', ItemCategory)


# item_categories = ItemCategories()
# print(item_categories.full_list())
# print()
# print(item_categories.search(id=1))
