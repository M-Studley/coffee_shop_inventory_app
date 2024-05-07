from dataclasses import dataclass
from database.database import Database
from data.utils import BaseManager

db = Database()


@dataclass
class Location:
    id: int
    _store_id: int
    address: str
    city: str
    state: str
    postal_code: int


class Locations(BaseManager):
    def __init__(self):
        super().__init__('location', Location)


# locations = Locations()
# print(locations.full_list())
# print()
# print(locations.search(id=2))


# class LocationManager:
#     @classmethod
#     def _create_location(cls, *,
#                          entity,
#                          address: str,
#                          city: str,
#                          state: str,
#                          postal_code: str) -> int:
#         location_query = """
#         INSERT INTO `location` (`address`, `city`, `state`, `postal_code`)
#         VALUES (%s, %s, %s, %s, %s)
#         """
#         location_data = (address, city, state, postal_code)
#         db.execute(location_query, location_data)
#         location_id_query = db.fetchone("SELECT LAST_INSERT_ID() AS `last_id` FROM `location`")
#         location_id = location_id_query['last_id']
#
#         return location_id
