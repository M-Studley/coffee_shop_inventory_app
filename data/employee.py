from dataclasses import dataclass
from functools import cached_property, cache
from database.database import Database
from data.store import Store, Stores

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


class Employees:
    @cached_property
    def full_list(self) -> list[Employee]:
        full_list = []
        query = "SELECT * FROM `employee`"
        all_rows = db.fetchall(query)
        for row in all_rows:
            employee = Employee(**row)
            store = Stores().search(id=employee._store_number_id)
            employee.store = store[0] if store else None
            full_list.append(employee)
        return full_list

    @cache
    def search(self, **kwargs) -> list[Employee]:
        results = self.full_list[:]
        for employee in self.full_list:
            for key in kwargs:
                try:
                    value = getattr(employee, key)
                except AttributeError:
                    raise Exception(f"Key '{key}' does not exist...")

                if value != kwargs[key]:
                    results.remove(employee)
                    break

        return results


# print(Employees().search(id=1))
