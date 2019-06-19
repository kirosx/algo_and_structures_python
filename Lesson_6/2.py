"""
2. Создать пользовательский класс данных (или использовать) один из классов,
реализованных в курсе Python.Основы. Реализовать класс с применением слотов
и обычным способом. Для объекта обычного класса проверить отображение словаря
атрибутов. Сравнить, сколько выделяется памяти для хранения атрибутов обоих
классов.
"""
from pympler import asizeof

class Rectangle:
 def __init__(self,width,length):
  self.width=width
  self.length=length
  self.square=self.length*self.width


class RectangleSlot:
 __slots__ = ['width','length','square']
 def __init__(self,width,length):
  self.width=width
  self.length=length
  self.square=self.width*self.length

rt = Rectangle(2,5)
rtslots = RectangleSlot(2,5)
print(asizeof.asizeof(rt))
print(asizeof.asizeof(rtslots))

# При использовании слотов памяти выделяется в 2.7 (!) раза меньше
