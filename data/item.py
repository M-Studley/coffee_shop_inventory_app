from dataclasses import dataclass
from functools import cache, cached_property
from database.database import Database

db = Database()


@dataclass
class Item:
    id: int
    name: str
    measurement_amount: int
    measurement_type: list
    sku: str


class Items:
    @cached_property
    def full_list(self) -> list[Item]:
        query = "SELECT * FROM `item`"
        all_rows = db.fetchall(query)
        return [Item(**row) for row in all_rows]

    @cache
    def search(self, **kwargs) -> list[Item] | list[str]:
        results = self.full_list[:]
        for item in self.full_list:
            for key in kwargs:
                try:
                    value = getattr(item, key)
                except AttributeError:
                    return [f"Key '{key}' does not exist..."]

                if value != kwargs[key]:
                    results.remove(item)
                    break

        return results
