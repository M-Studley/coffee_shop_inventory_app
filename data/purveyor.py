from dataclasses import dataclass
from database.database import Database
from data.purveyor_login import PurveyorLogins
from data.item import Items
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

    @property
    def items(self):
        return Items().search(_purveyor_id=self.id)


class Purveyors(Searchable):
    child = Purveyor
