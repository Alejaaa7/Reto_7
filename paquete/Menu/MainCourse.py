# MainCourse.py

from .MenuItem import MenuItem

class MainCourse(MenuItem):
    def __init__(self, name: str, price: float, type_of_cooking: str):
        super().__init__(name, price)
        self.type_of_cooking = type_of_cooking

        