from dataclasses import dataclass
from data.utils import DataManager


@dataclass
class ItemCategory:
    id: int
    name: str
    description: str
    
    
class ItemCategories(DataManager):
    child = ItemCategory
