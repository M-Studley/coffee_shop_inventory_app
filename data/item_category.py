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
    @classmethod
    def search(cls, **kwargs):
        return BaseManager.search(**kwargs)


# item_categories = ItemCategories()
# print(item_categories.search(model_class=ItemCategory, table='item_category'))
