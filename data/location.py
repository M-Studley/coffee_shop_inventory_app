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


class LocationManager:
    @classmethod
    def _create_location(cls, *,
                         entity,
                         address: str,
                         city: str,
                         state: str,
                         postal_code: str) -> int:
        location_query = """
        INSERT INTO `location` (`address`, `city`, `state`, `postal_code`)
        VALUES (%s, %s, %s, %s, %s)
        """
        location_data = (address, city, state, postal_code)
        db.execute(location_query, location_data)
        location_id_query = db.fetchone("SELECT LAST_INSERT_ID() AS `last_id` FROM `location`")
        location_id = location_id_query['last_id']

        return location_id


# locations = Locations()
# print(locations.search(id=1, address='123 Main st.'))
