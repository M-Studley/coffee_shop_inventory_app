from functools import cached_property, cache
from database.database import Database

db = Database()


class BaseManager:
    def __init__(self, table_name: str, model_class):
        self.table = table_name
        self.model_class = model_class

    # @cached_property
    def full_list(self) -> list:
        query = f"SELECT * FROM `{self.table}`"
        all_rows = db.fetchall(query)
        return [self.model_class(**row) for row in all_rows]

    @cache
    def search(self, **kwargs) -> list:
        results = self.full_list()
        for item in results:
            for key in kwargs:
                try:
                    value = getattr(item, key)
                except AttributeError:
                    raise Exception(f"Key '{key}' does not exist...")

                if value != kwargs[key]:
                    results.remove(item)
                    break

        return results
