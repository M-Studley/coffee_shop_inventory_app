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
    purveyor: Purveyor = None
    inventory: Inventory = None


class Items(BaseManager):
    def __init__(self):
        super().__init__('item', Item)

    def full_list(self) -> list:
        full_list = super().full_list()
        for item in full_list:
            item.category = next((c for c in ItemCategories().search(id=item._category_id)), None)
            item.info = next((c for c in ItemInfos().search(_item_id=item.id)), None)
            item.purveyor = next((c for c in Purveyors().search(id=item._purveyor_id)), None)
            item.inventory = next((c for c in Inventories().search(id=item._inventory_id)), None)

        return full_list


# items = Items()
# print(items.full_list())
# print()
# print(items.search(id=1))
