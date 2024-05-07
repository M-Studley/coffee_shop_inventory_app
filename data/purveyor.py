from dataclasses import dataclass
from database.database import Database
from data.purveyor_login import PurveyorLogin, PurveyorLogins
from data.utils import BaseManager

db = Database()


@dataclass
class Purveyor:
    id: int
    name: str
    url: str
    email: str
    login: PurveyorLogin = None


class Purveyors(BaseManager):
    def __init__(self):
        super().__init__('purveyor', Purveyor)

    def full_list(self) -> list:
        full_list = super().full_list()
        for purveyor in full_list:
            purveyor.login = next((c for c in PurveyorLogins().search(_purveyor_id=purveyor.id)), None)

        return full_list


# purveyors = Purveyors()
# print(purveyors.full_list())
# print()
# print(purveyors.search(id=1))
