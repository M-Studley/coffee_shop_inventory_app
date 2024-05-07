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


# print(PurveyorLogins().full_list)
# print(PurveyorLogins().search(id=1))

# class PurveyorLogins:
#     @cached_property
#     def full_list(self) -> list[PurveyorLogin]:
#         query = "SELECT * FROM `purveyor_login`"
#         all_rows = db.fetchall(query)
#         return [PurveyorLogin(**row) for row in all_rows]
# 
#     @cache
#     def search(self, **kwargs) -> list[PurveyorLogin] | list[str]:
#         results = self.full_list[:]
#         for purveyor_login in self.full_list:
#             for key in kwargs:
#                 try:
#                     value = getattr(purveyor_login, key)
#                 except AttributeError:
#                     return [f"Key '{key}' does not exist..."]
# 
#                 if value != kwargs[key]:
#                     results.remove(purveyor_login)
#                     break
# 
#         return results
