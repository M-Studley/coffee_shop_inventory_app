from dataclasses import dataclass
from data.utils import Searchable


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


print(Locations().search())
