from dataclasses import dataclass
from data.utils import DataManager


@dataclass
class Location:
    id: int
    _store_id: int
    address: str
    city: str
    state: str
    postal_code: int


class Locations(DataManager):
    child = Location
