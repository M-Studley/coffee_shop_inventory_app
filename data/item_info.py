from dataclasses import dataclass
from functools import cache, cached_property
from database.database import Database

db = Database()


@dataclass
class ItemInfo:
    id: int
    price: float
    purchase_date: str
    checked_in: str
    checked_out: str
    order_status: str


class ItemInfos:
    @cached_property
    def full_list(self) -> list[ItemInfo]:
        query = "SELECT * FROM `item_info`"
        all_rows = db.fetchall(query)
        return [ItemInfo(**row) for row in all_rows]

    @cache
    def search(self, **kwargs) -> list[ItemInfo] | list[str]:
        results = self.full_list[:]
        for item_info in self.full_list:
            for key in kwargs:
                try:
                    value = getattr(item_info, key)
                except AttributeError:
                    return [f"Key '{key}' does not exist..."]

                if value != kwargs[key]:
                    results.remove(item_info)
                    break

        return results
