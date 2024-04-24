from dataclasses import dataclass
from functools import cached_property, cache
from database.database import Database
from data.location import Location, Locations, LocationManager

db = Database()
locations = Locations()


@dataclass
class Store:
    id: int
    number: int
    name: str
    phone: str
    location: Location = None


class Stores:
    @cached_property
    def full_list(self) -> list[Store]:
        full_list = []
        query = "SELECT * FROM `store`"
        all_rows = db.fetchall(query)
        for row in all_rows:
            store = Store(**row)
            my_location = locations.search(_store_id=store.id)
            store.location = my_location[0] if my_location else None
            full_list.append(store)
        return full_list

    @cache
    def search(self, **kwargs) -> list[Store] | list[str]:
        results = self.full_list[:]
        for store in self.full_list:
            for key in kwargs:
                try:
                    value = getattr(store, key)
                except AttributeError:
                    return [f"Key '{key}' does not exist..."]

                if value != kwargs[key]:
                    results.remove(store)
                    break
        return results


class StoreManager:
    @staticmethod
    def create_store_with_location(*, number: int,
                                   name: str,
                                   phone: str,
                                   address: str,
                                   city: str,
                                   state: str,
                                   postal_code: str) -> int:

        existing_store = Locations().search(address=address)
        if existing_store:
            raise ValueError("A store with the same address already exists.")

        store_query = """
        INSERT INTO `store` (`number`, `name`, `phone`)
        VALUES (%s, %s, %s)
        """
        store_data = (number, name, phone)
        db.execute(store_query, store_data)
        store_id_query = db.fetchone("SELECT MAX(`id`) FROM `store`")
        store_id = store_id_query['MAX(`id`)']

        LocationManager._create_location(store_id=store_id,
                                         address=address,
                                         city=city,
                                         state=state,
                                         postal_code=postal_code)

        return store_id


# stores = Stores()
store_manager = StoreManager()
print(store_manager.create_store_with_location(number=4,
                                               name='Test Store #4',
                                               phone='666-666-6666',
                                               address='777 7th st.',
                                               city='Test City',
                                               state='TS',
                                               postal_code='66666'))

