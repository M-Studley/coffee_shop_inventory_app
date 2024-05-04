from dataclasses import dataclass
from functools import cache, cached_property
from database.database import Database
from data.item_category import ItemCategory, ItemCategories
from data.item_info import ItemInfo, ItemInfos
from data.purveyor import Purveyor, Purveyors
from data.inventory import Inventory, Inventories
from data.employee import Employee, Employees

db = Database()


@dataclass
class Item:
    id: int
    _employee_id: int
    name: str
    _item_category_id: int
    measurement_amount: int
    measurement_type: list
    _purveyor_id: int
    sku: str
    _inventory_id: int
    employee: Employee = None
    item_category: ItemCategory = None
    item_info: ItemInfo = None
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
            employee = Employees().search(id=item._employee_id)
            item_category = ItemCategories().search(id=item._item_category_id)
            item_info = ItemInfos().search(_item_id=item.id)
            purveyor = Purveyors().search(id=item._purveyor_id)
            inventory = Inventories().search(id=item._inventory_id)
            item.employee = employee[0] if employee else None
            item.item_category = item_category[0] if item_category else None
            item.item_info = item_info[0] if item_category else None
            item.purveyor = purveyor[0] if purveyor else None
            item.inventory = inventory[0] if inventory else None
            full_list.append(item)
        return full_list

    @cache
    def search(self, **kwargs) -> list[Item] | list[str]:
        results = self.full_list[:]
        for item in self.full_list:
            for key in kwargs:
                try:
                    value = getattr(item, key)
                except AttributeError:
                    return [f"Key '{key}' does not exist..."]

                if value != kwargs[key]:
                    results.remove(item)
                    break

        return results


print(Items().full_list)
