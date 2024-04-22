from dataclasses import dataclass
from functools import cached_property, cache
from database.database import Database
from data.location import Location, Locations

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
    def full_list(self):
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
    def search(self, **kwargs) -> list:
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


# stores = Stores()
# print(stores.search(phone='603-222-2222'))
