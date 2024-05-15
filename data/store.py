from dataclasses import dataclass
from database.database import Database
from data.location import Locations
from data.inventory import Inventories
from data.employee import Employees
from data.utils import Searchable

db = Database()


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


# print(Stores().search())
# print()
# for store in Stores().search(id=1):
#     print(store.location)
#     print(store.inventory)
#     print(store.employees)


# class StoreManager:;
#     @classmethod
#     def create_store_with_location(cls, *,
#                                    number: int,
#                                    name: str,
#                                    phone: str,
#                                    address: str,
#                                    city: str,
#                                    state: str,
#                                    postal_code: str) -> int:
#         existing_store = Locations().search(address=address)
#
#         if existing_store:
#             raise ValueError("A store with the same address already exists.")
#
#         store_query = """
#         INSERT INTO `store` (`number`, `name`, `phone`)
#         VALUES (%s, %s, %s)
#         """
#         store_data = (number, name, phone)
#         db.execute(store_query, store_data)
#         store_id_query = db.fetchone("SELECT LAST_INSERT_ID() AS `last_id` FROM `store`")
#         store_id = store_id_query['last_id']
#
#         entity = Stores().search(id=store_id)
#
#         LocationManager._create_location(entity=entity[0],
#                                          address=address,
#                                          city=city,
#                                          state=state,
#                                          postal_code=postal_code)
#
#         return store_id


# print(StoreManager().create_store_with_location(number=5,
#                                                 name='Test Store #5',
#                                                 phone='555-555-5555',
#                                                 address='555 5th st.',
#                                                 city='Test City',
#                                                 state='TS',
#                                                 postal_code='55555'))
