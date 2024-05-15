from dataclasses import dataclass
from database.database import Database
from data.utils import BaseManager

db = Database()


@dataclass
class PurveyorLogin:
    id: int
    user_name: str
    password: str
    _purveyor_id: int
    
    
class PurveyorLogins(BaseManager):
    @classmethod
    def search(cls, **kwargs):
        return BaseManager.search(**kwargs)


# purveyor_logins = PurveyorLogins()
# print(purveyor_logins.search(model_class=PurveyorLogin, table='purveyor_login'))
