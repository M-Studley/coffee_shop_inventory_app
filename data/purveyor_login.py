from dataclasses import dataclass
from data.utils import DataManager


@dataclass
class PurveyorLogin:
    id: int
    user_name: str
    password: str
    _purveyor_id: int
    
    
class PurveyorLogins(DataManager):
    child = PurveyorLogin
