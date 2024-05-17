from dataclasses import dataclass
from data.utils import Searchable


@dataclass
class ItemCategory:
    id: int
    name: str
    description: str
    
    
class ItemCategories(Searchable):
    child = ItemCategory
