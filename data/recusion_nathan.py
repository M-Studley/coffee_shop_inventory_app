from dataclasses import dataclass
from functools import cached_property


@dataclass
class YetAnotherClass:
    library: str


class AnotherClass:
    def __init__(self, *, book, publish_year, library_details):
        self.book: str = book
        self.publish_year: int = publish_year
        self.library_details: YetAnotherClass = library_details

    @cached_property
    def what_book(self):
        return self.library_details


@dataclass
class MyDataClass:
    name: str
    age: int
    address: str
    email: str
    favorite_book: AnotherClass

    @property
    def my_property(self):
        return 'im a property'


# def my_func(something):
#     if isinstance(something, tuple):
#         return tuple(my_func(item) for item in something)
#     elif isinstance(something, list):
#         return list(my_func(item) for item in something)
#     elif hasattr(something, '__dict__'):
#         return {item: my_func(getattr(something, item))
#                 for item in something.__dir__()
#                 if not item.startswith('_')}
#     else:
#         return something


my_yet_another_class = YetAnotherClass(library='The Main Library')
my_another_class = AnotherClass(book='On the Road',
                                publish_year=9999,
                                library_details=my_yet_another_class)

my_class = MyDataClass(name='Michael',
                       age=99,
                       address='123 Main St.',
                       email='email@email.com',
                       favorite_book=my_another_class)
class_result = my_func(my_class)
print(class_result)
# print()
# my_tuple = (1, 2, my_class, ['im', 'a', 'list'], 'string', True, {'my_dict': 3}, (1, 2))
# tuple_result = my_func(my_tuple)
# print(tuple_result)
