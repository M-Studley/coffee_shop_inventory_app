from dataclasses import dataclass


class TestClass:
    class_var = 'class variable'

    @property
    def test(self):
        prop_var = 'PROP VARIABLE'
        return [f'**{prop_var}**, This is a TestClass']


@dataclass
class TestDataclass:
    name: tuple
    age: int
    country: str
    other: TestClass

    @property
    def test_property(self):
        prop_var = 'PROP VARIABLE'
        return [f'**{prop_var}**, This is a TestDataclass']


x = TestDataclass(name=('test', 'name'), age=99, country='test country', other=TestClass())
y = TestClass()


# for item in x.__dir__():
#     if item.startswith('__'):
#         continue
#     else:
#         result = str(type(getattr(x, item)))[8:-2]
#         print(result)


# print(x.__dir__())
# print()
# print(TestDataclass.__dir__(TestDataclass))
#
# print()
# print(y.__dir__())
# print()
# print(TestClass.__dir__(TestClass))
