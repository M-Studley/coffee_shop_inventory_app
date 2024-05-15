from dataclasses import dataclass
from database.database import Database
from data.purveyor_login import PurveyorLogins
from data.utils import Searchable

db = Database()


@dataclass
class Purveyor:
    id: int
    name: str
    url: str
    email: str

    @property
    def purveyor_login(self):
        return PurveyorLogins().search(_purveyor_id=self.id)


class Purveyors(Searchable):
    child = Purveyor


# print(Purveyors().search())
# for purveyor in Purveyors().search(id=2):
#     print(purveyor.purveyor_login)
