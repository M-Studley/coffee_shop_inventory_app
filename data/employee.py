from dataclasses import dataclass
from database.database import Database
from data.store import Store, Stores
from data.utils import BaseManager

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
    store: Store = None


class Employees(BaseManager):
    pass


# employees = Employees()
# print(employees.full_list())
# print()
# print(employees.search(id=2))
