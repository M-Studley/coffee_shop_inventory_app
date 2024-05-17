from dataclasses import dataclass
from data.location import Locations
from data.inventory import Inventories
from data.employee import Employees
from data.utils import Searchable


@dataclass
class Store:
    id: int
    number: int
    name: str
    phone: str

    @property
    def location(self):
        return Locations().search(_store_id=self.id)

    @property
    def inventory(self):
        return Inventories().search(_store_id=self.id)

    @property
    def employees(self):
        return Employees().search(_store_number_id=self.id)


class Stores(Searchable):
    child = Store
