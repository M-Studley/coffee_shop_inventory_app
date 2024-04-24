from dataclasses import dataclass
from database.database import Database
from functools import cache, cached_property

db = Database()


@dataclass
class User:
    id: int
    first_name: str
    last_name: str
    password: str
    email: str
    permission_level: int


class Users:
    @cached_property
    def full_list(self) -> list[User]:
        query = "SELECT * FROM `user`"
        all_rows = db.fetchall(query)
        return [User(**row) for row in all_rows]

    @cache
    def search(self, **kwargs):
        results = self.full_list[:]
        for user in self.full_list:
            for key in kwargs:
                try:
                    value = getattr(user, key)
                except AttributeError:
                    return [f"Key '{key}' does not exist..."]

                if value != kwargs[key]:
                    results.remove(user)
                    break

        return results


users = Users()
print(users.search())
