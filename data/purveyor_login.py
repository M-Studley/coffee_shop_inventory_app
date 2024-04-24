from dataclasses import dataclass
from functools import cache, cached_property
from database.database import Database

db = Database()


@dataclass
class PurveyorLogin:
    id: int
    name: str
    password: str


class PurveyorLogins:
    @cached_property
    def full_list(self) -> list[PurveyorLogin]:
        query = "SELECT * FROM `purveyor_login`"
        all_rows = db.fetchall(query)
        return [PurveyorLogin(**row) for row in all_rows]

    @cache
    def search(self, **kwargs) -> list[PurveyorLogin] | list[str]:
        results = self.full_list[:]
        for purveyor_login in self.full_list:
            for key in kwargs:
                try:
                    value = getattr(purveyor_login, key)
                except AttributeError:
                    return [f"Key '{key}' does not exist..."]

                if value != kwargs[key]:
                    results.remove(purveyor_login)
                    break

        return results
