from dataclasses import dataclass
from database.database import Database
from data.purveyor_login import PurveyorLogin
from data.utils import BaseManager

db = Database()


@dataclass
class Purveyor:
    id: int
    name: str
    url: str
    email: str

    @property
    def purveyor_login(self):
        return next(iter(BaseManager().search(
            table='purveyor_login',
            model_class=PurveyorLogin,
            _purveyor_id=self.id)
        ), None)


class Purveyors(BaseManager):
    @classmethod
    def search(cls, **kwargs):
        return BaseManager.search(table='purveyor', model_class=Purveyor, **kwargs)


# print(Purveyors.search())
# for purveyor in Purveyors().search(id=1):
#     print(purveyor.purveyor_login)
