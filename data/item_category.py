from dataclasses import dataclass
from functools import cache, cached_property
from database.database import Database

db = Database()


@dataclass
class ItemCategory:
    id: int
    name: str
    description: str


class ItemCategories:
    @cached_property
    def full_list(self) -> list[ItemCategory]:
        query = "SELECT * FROM `item_category`"
        all_rows = db.fetchall(query)
        return [ItemCategory(**row) for row in all_rows]

    @cache
    def search(self, **kwargs) -> list[ItemCategory] | list[str]:
        results = self.full_list[:]
        for category in self.full_list:
            for key in kwargs:
                try:
                    value = getattr(category, key)
                except AttributeError:
                    return [f"Key '{key}' does not exists..."]

                if value != kwargs[key]:
                    results.remove(category)
                    break

        return results
