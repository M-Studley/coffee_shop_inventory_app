from dataclasses import dataclass
from data.item_category import ItemCategories
from data.item_info import ItemInfos
from data.utils import Searchable


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

    @property
    def item_category(self):
        return ItemCategories().search(id=self._category_id)

    @property
    def item_info(self):
        return ItemInfos().search(id=self._category_id)


class Items(Searchable):
    child = Item
