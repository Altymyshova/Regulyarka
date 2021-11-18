class Myclass():
    @staticmethod
    def staticmethod():
        print('static method called')

    @property
    def property():
        print('property method called')

class MyClass():
    
    TOTAL_OBJECTS=0
    
    def __init__(self):
        MyClass.TOTAL_OBJECTS = MyClass.TOTAL_OBJECTS+1
    
    @classmethod
    def total_objects(cls):
        print("Total objects: ",cls.TOTAL_OBJECTS)
# Создаем объекты        
my_obj1 = MyClass()
my_obj2 = MyClass()
my_obj3 = MyClass()
my_obj4 = MyClass()
# Вызываем classmethod 
MyClass.total_objects()


import random

class TimeDesk:
    def __init__(self, seconds):
        self.seconds = seconds

    def time_2(self):
        min = self.seconds // 60
        self.seconds -= 60*min

        hours = self.seconds // 3600
        self.seconds -= 3600*hours

        day = self.seconds // 86400
        self.seconds -= 86400*day

        general_resultat = (f'day: {day}, hours: {hours} min: {min}, seconds: {self.seconds}')
        return general_resultat


timed = TimeDesk(78965)
timed.time_2()

