from dataclasses import dataclass
from data.purveyor_login import PurveyorLogins
from data.item import Items
from data.utils import Searchable


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
