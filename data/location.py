from dataclasses import dataclass
from database.database import Database
from data.utils import Searchable

db = Database()


@dataclass
class Location:
    id: int
    _store_id: int
    address: str
    city: str
    state: str
    postal_code: int


class Locations(Searchable):
    child = Location
