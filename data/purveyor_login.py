from dataclasses import dataclass
from database.database import Database
from data.utils import Searchable

db = Database()


@dataclass
class PurveyorLogin:
    id: int
    user_name: str
    password: str
    _purveyor_id: int
    
    
class PurveyorLogins(Searchable):
    child = PurveyorLogin


# pur_log = PurveyorLogins()
# print(pur_log.search())
