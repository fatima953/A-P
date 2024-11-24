#Abstaction
from abc import ABC, abstractmethod
class animal(ABC):
    def move(self):
        pass
class human(animal):
    def move(self):
     print("i can walk and run")
class snake(animal):
  def move(self):
     print("i can crawl")
class cat(animal):
  def move(self):
     print("i can miao")
h = human()
h.move()
s = snake()
s.move()
c = cat()
c.move()

#Polymorphism
class Pakistan:
   def capital(self):
      print("the capital is Islamabad")
   def language(self):
      print("Urdu is the language of pakistan")
class China:
   def capital(self):
      print("the capital of China is 北京")
   def language(self):
      print("the language of China is mandrin")

p = Pakistan()
p.capital()
p.language()
c = China()
c.capital()
c.language()
