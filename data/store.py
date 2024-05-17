from dataclasses import dataclass
from data.location import Locations
from data.inventory import Inventories
from data.employee import Employees
from data.utils import Searchable
from database.database import Database as db


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

    def update(self, **kwargs):
        set_statement = ', '.join([f"`{key}` = '{value}'" for key, value in kwargs.items()])
        query = f"""
        UPDATE `{self.__class__.__name__.lower()}`
        SET {set_statement}
        WHERE `id` = %s;
        """
        values = (self.id,)
        db.execute(query, values)


class Stores(Searchable):
    child = Store


my_store = next(iter(Stores().search(id=2)))
print(my_store)
my_store.update(name='peets coffee', phone="111-222-3333")
changed = next(iter(Stores().search(id=2)))
print(changed)
