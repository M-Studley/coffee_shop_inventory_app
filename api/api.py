from flask import Flask
from functools import cache
import json
from database.database import Database
from data.store import Stores

db = Database()


class API:

    @cache
    def stores(self, **kwargs):
        stores = Stores()
        return stores.search(**kwargs)

    def serialize_data(self, data):
        if isinstance(data, tuple):
            return tuple(self.serialize_data(item) for item in data)
        elif isinstance(data, list):
            return list(self.serialize_data(item) for item in data)
        elif hasattr(data, '__dict__'):
            return {item: self.serialize_data(getattr(data, item))
                    for item in data.__dir__()
                    if not item.startswith('_')}
        else:
            return data


api = API()
app = Flask(__name__)


@app.route('/stores')
def return_json():
    return json.dumps(api.serialize_data(api.stores()))


app.run()
