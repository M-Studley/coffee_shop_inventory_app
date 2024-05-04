from dataclasses import dataclass
from functools import cache, cached_property
from database.database import Database
from data.purveyor_login import PurveyorLogin, PurveyorLogins

db = Database()


@dataclass
class Purveyor:
    id: int
    name: str
    url: str
    email: str
    login: PurveyorLogin = None


class Purveyors:
    @cached_property
    def full_list(self) -> list[Purveyor]:
        full_list = []
        query = "SELECT * FROM `purveyor`"
        all_rows = db.fetchall(query)
        for row in all_rows:
            purveyor = Purveyor(**row)
            purveyor_login = PurveyorLogins().search(_purveyor_id=purveyor.id)
            purveyor.login = purveyor_login[0] if purveyor_login else None
            full_list.append(purveyor)
        return full_list

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
