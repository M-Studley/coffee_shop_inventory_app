from dataclasses import dataclass
from database.database import Database
from data.item_category import ItemCategory, ItemCategories
from data.item_info import ItemInfo, ItemInfos
from data.purveyor import Purveyor, Purveyors
from data.inventory import Inventory, Inventories
from data.utils import BaseManager

db = Database()


@dataclass
class Item:
    id: int
    _employee_id: int
    name: str
    _category_id: int
    measurement_amount: int
    measurement_type: list
    _purveyor_id: int
    sku: str
    _inventory_id: int
    category: ItemCategory = None
    info: ItemInfo = None
    # purveyor: Purveyor = None
    # inventory: Inventory = None


class Items(BaseManager):
    pass
