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
    def __init__(self):
        super().__init__('purveyor_login', PurveyorLogin)


print(PurveyorLogins().full_list())
print(PurveyorLogins().search(id=1))
