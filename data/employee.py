from dataclasses import dataclass
from data.utils import DataManager


@dataclass
class Employee:
    id: int
    _store_number_id: int
    first_name: str
    last_name: str
    password: str
    email: str
    permission_level: int


class Employees(DataManager):
    child = Employee
