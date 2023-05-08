
class Student:
    def __init__(self, id, name):
        self.id = id
        self.__name = name

    def __str__(self):
        return self.__name

obj = Student("21911407", "양재서") 
print(obj)

# # print(obj.__name) // 에러 발생!!!!
# print(dir(obj)) # 클래스 속성 출력
# print(obj._Student__age) # 보려면 볼 수는 있다. private라고 하기에는 다소 허술하다.

# print(obj)

# list_array = [str, int, list, tuple, type(None), object, type]
# for i in dir(object) :
#     if (type(object.__getattribute__(object, i)) in list_array) :
#         print(i)  

import Calc

class Animal:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def eat(self):
        print("먹기")

    def unit_sub(self):
        return Calc.Calc().multiple(self.weight)


class Cat(Animal):
    def __init__(self, name, breeds, weight):
        super().__init__(name, weight)
        self.breed = breeds

    def claw(self):
        print("할퀴기")

    def meow(self):
        print("야옹")

    def __str__(self):
        return self.name
    
cat = Cat("나비", "페르시안", 3.5)
print(cat.unit_sub())

cat.eat()
cat.meow()

