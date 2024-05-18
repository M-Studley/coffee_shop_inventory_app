import re
from database.database import Database as dB


def update_instance(instance, **kwargs):
    set_statement = ', '.join([f"`{key}` = %s" for key in kwargs.keys()])
    query = f"""
    UPDATE `{instance.__class__.__name__.lower()}`
    SET {set_statement}
    WHERE `id` = %s;
    """
    values = tuple(kwargs.values()) + (instance.id,)
    dB.execute(query, values)


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
        all_rows = dB.fetchall(query)
        results = [self.child(**row) for row in all_rows] # noqa

        for item in results[:]:
            for key in kwargs:
                if not hasattr(item, key): raise Exception(f"Key '{key}' does not exist...") # noqa

                value = getattr(item, key)

                if value != kwargs[key]:
                    results.remove(item)
                    break

        return results
