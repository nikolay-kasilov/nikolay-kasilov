'''
*
**
***
****
'''
def f(size):
    for i in range(1,size+1):
        print(i*"*")
f(4)
f(7)
f(6)
'''
5
*****
*   *
*   *
*   *
*****
'''
def f(size):
    if size <= 0:
        return
    if size == 1:
        print("#")
        return
    print((size  )*'#')
    for _ in range(size -2 ):
        print((size -2)* '#')* " "+ "*"
    print(size *'#')
print('_')
f(0)
f(1)
f(2)
f(4)


class Cat:
    def meow(self):
        print("Мяу!")

cat = Cat()
cat.meow()
cat2 = Cat()
cat.meow()



class Cat():
    def __int__(self, name):
        self.name = name
    def meow(self):
        print(f"{self.name}: Мяу!")

cat = Cat("Барсик")
cat2 = Cat("Мурзик")
cat.meow()
cat2.meow()

class Student():
    def __init__(self, full_name, age, course):
        self.full_name = full_name
        self.age = age
        self.course = course

    def info(self):
        return f"{self.full_name}, {self.age}, {self.course}"

student = Student(full_name="iv iv iv",age="23",course="5")
student.info()

print(student.info())

class Field:
    def __init__(self):
        self.field = [' '] * 9
    def _check(self, index):
        return self.field[index] == ' '
    def turn(self, index, symbol):
        if self._check(index):
            self.field[index] = symbol
        else:
            print("Ячейка уже занята")
    def print(self):
        print(self.field[:3])
        print(self.field[3:6])
        print(self.field[6:])
        print()

field = Field()
field.print()
field.turn(3, 'X')
field.print()
field.turn(3, '0')
field.print()

   #25 12 2023

from    datetime import date
class Person:
    def __init__(self, first_name, last_name, birthday):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    def get_age(self):
        return (date.today() - self.birthday).days // 365.25
    def info(self):
        return f"{self.get_full_name()}: {self.get_age()} лет"

sasha = Person("Саша", "Сашин", date(1990, 12, 12))
print(sasha.info())
  #25 .12 .23
import json


class BaseFileHandler:
    def __init__(self, path: str):
        """

        :type path: object
        """
        self._path = path

    def read(self, data: str) -> dict:
        with open(self._path, 'r', encoding='utf-8') as f:
            return self._deserialize(f.read())

    def _deserialize(self, data: str) -> dict:
        return {}

    def write(self, data: dict):
        with open(self._path, 'w', encoding='utf-8') as f:
            f.write(self._serialize(data))

    def _serialize(self, data: dict) -> str:
        return ','.join(f"{key}:{value}" for key, value in data.items())


class TXTFileHandler(BaseFileHandler):
    def _serialize(self, data: dict) -> str:
        return ','.join(f"{key}:{value}" for key, value in data.items())


class JSONFileHandler(BaseFileHandler):
    def _serialize(self, data: dict) -> str:
        return json.dumps(data)

    def _deserialize(self, data: str) -> dict:
        return json.loads(data)


    def write(self, student):
        pass


student = {"name": "Василий", "group": "P33"}

txt_handler = TXTFileHandler("student.txt")
txt_handler.write(student)
print(f"TXT: {txt_handler.read(student)}")
json_handler = JSONFileHandler("student.json")
json_handler.write(student)
print(f"JSON: {json_handler.read(student)}")

   
    
