from dataclasses import dataclass
from functools import cache, cached_property
from database.database import Database
from data.item_category import ItemCategory, ItemCategories
from data.item_info import ItemInfo, ItemInfos
from data.purveyor import Purveyor, Purveyors
from data.inventory import Inventory, Inventories

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


class Items:
    @cached_property
    def full_list(self) -> list[Item]:
        full_list = []
        query = "SELECT * FROM `item`"
        all_rows = db.fetchall(query)
        for row in all_rows:
            item = Item(**row)
            item.category = next((c for c in ItemCategories().search(id=item._category_id)), None)
            item.info = next((c for c in ItemInfos().search(_item_id=item.id)), None)
            item.purveyor = next((c for c in Purveyors().search(id=item._purveyor_id)), None)
            item.inventory = next((c for c in Inventories().search(id=item._inventory_id)), None)
            full_list.append(item)
        return full_list

    @cache
    def search(self, **kwargs) -> list[Item]:
        results = self.full_list[:]
        for item in self.full_list:
            for key in kwargs:
                try:
                    value = getattr(item, key)
                except AttributeError:
                    raise Exception(f"Key '{key}' does not exist...")

                if value != kwargs[key]:
                    results.remove(item)
                    break

        return results


# print(Items().full_list)
# print(Items().search(id=2))
