import re
from database.database import Database

db = Database()


class Searchable:
    @property
    def camel_to_snake_case(self):
        table_name = re.sub(r'ies$', 'y', self.__class__.__name__)
        table_name = re.sub(r's$', '', table_name)
        table_name = re.sub(r'(?<=[a-z])(?=[A-Z])', '_', table_name).lower()
        return table_name

    def search(self, **kwargs):
        table_name = self.camel_to_snake_case
        query = f"SELECT * FROM `{table_name}`"
        all_rows = db.fetchall(query)
        results = [self.child(**row) for row in all_rows] # noqa

        for item in results[:]:
            for key in kwargs:
                if not hasattr(item, key): raise Exception(f"Key '{key}' does not exist...")

                value = getattr(item, key)

                if value != kwargs[key]:
                    results.remove(item)
                    break

        return results
