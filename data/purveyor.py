from dataclasses import dataclass
from functools import cache, cached_property
from database.database import Database

db = Database()


@dataclass
class Purveyor:
    id: int
    name: str
    url: str
    email: str


class Purveyors:
    @cached_property
    def full_list(self) -> list[Purveyor]:
        query = "SELECT * FROM `purveyor`"
        all_rows = db.fetchall(query)
        return [Purveyor(**row) for row in all_rows]

    @cache
    def search(self, **kwargs) -> list[Purveyor] | list[str]:
        results = self.full_list[:]
        for purveyor in self.full_list:
            for key in kwargs:
                try:
                    value = getattr(purveyor, key)
                except AttributeError:
                    return [f"Key '{key}' does not exist..."]

                if value != kwargs[key]:
                    results.remove(purveyor)
                    break

        return results
