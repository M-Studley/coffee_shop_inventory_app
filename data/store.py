from dataclasses import dataclass
from database.database import Database
from data.location import Location, Locations
from data.utils import BaseManager

db = Database()


@dataclass
class Store:
    id: int
    number: int
    name: str
    phone: str
    location: Location = None


class Stores(BaseManager):
    def __init__(self):
        super().__init__('store', Store)

    def full_list(self) -> list:
        full_list = super().full_list()
        for store in full_list:
            store.location = next((c for c in Locations().search(_store_id=store.id)), None)

        return full_list


# stores = Stores()
# print(stores.full_list())
# print()
# print(stores.search(id=1))


# class StoreManager:
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
