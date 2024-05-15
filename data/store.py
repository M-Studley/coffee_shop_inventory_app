from dataclasses import dataclass
from database.database import Database
from data.location import Location
from data.utils import BaseManager

db = Database()


@dataclass
class Store:
    id: int
    number: int
    name: str
    phone: str

    @property
    def location(self):
        return next(iter(BaseManager().search(
            table='location',
            model_class=Location,
            _store_id=self.id)
        ), None)


class Stores(BaseManager):
    @classmethod
    def search(cls, **kwargs):
        return BaseManager.search(table='store', model_class=Store, **kwargs)


# print(Stores.search(id=2))
# print()
# for store in Stores().search(id=2):
#     print(store.location)


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
