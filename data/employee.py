from dataclasses import dataclass
from database.database import Database
# from data.store import Stores
from data.utils import Searchable

db = Database()


@dataclass
class Employee:
    id: int
    _store_number_id: int
    first_name: str
    last_name: str
    password: str
    email: str
    permission_level: int


class Employees(Searchable):
    child = Employee


# print(Employees().search())

