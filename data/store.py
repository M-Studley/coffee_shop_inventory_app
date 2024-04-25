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
    @classmethod
    def create_store_with_location(cls, *,
                                   number: int,
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
        store_id_query = db.fetchone("SELECT MAX(`id`) AS `max_id` FROM `store`")
        store_id = store_id_query['max_id']

        LocationManager._create_location(store_id=store_id,
                                         address=address,
                                         city=city,
                                         state=state,
                                         postal_code=postal_code)

        return store_id


print(StoreManager().create_store_with_location(number=4,
                                                name='Test Store #1',
                                                phone='111-111-1111',
                                                address='111 1th st.',
                                                city='Test City',
                                                state='TS',
                                                postal_code='11111'))
