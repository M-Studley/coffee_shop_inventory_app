from dataclasses import dataclass
from functools import cached_property, cache
from database.database import Database

db = Database()


@dataclass
class Location:
    id: int
    _store_id: int
    address: str
    city: str
    state: str
    postal_code: int


class Locations:
    @cached_property
    def full_list(self) -> list[Location]:
        query = "SELECT * FROM `location`"
        all_rows = db.fetchall(query)
        return [Location(**row) for row in all_rows]

    @cache
    def search(self, **kwargs) -> list[Location] | list[str]:
        results = self.full_list[:]
        for location in self.full_list:
            for key in kwargs:
                try:
                    value = getattr(location, key)
                except AttributeError:
                    return [f"Key '{key}' does not exist..."]

                if value != kwargs[key]:
                    results.remove(location)
                    break

        return results


# locations = Locations()
#
# print(locations.search(id=1, address='123 Main st.'))
