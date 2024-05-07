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
    def __init__(self):
        super().__init__('employee', Employee)

    def full_list(self) -> list:
        full_list = super().full_list()
        for employee in full_list:
            employee.store = next((c for c in Stores().search(id=employee._store_number_id)), None)

        return full_list


# employees = Employees()
# print(employees.full_list())
# print()
# print(employees.search(id=2))
