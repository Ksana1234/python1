#Есть класс Animal c одним методом voice().
class Animal:
    def voice(self):
        pass

class Dog(Animal):
    def voice(self):
        print('woof, woof, woof')


class Cat(Animal):
    def voice(self):
        print('meow, meow, moew')


class Bee(Animal):
    def voice(self):
        print('buzz, buzz, buzz, buzz')


d=Dog()
c=Cat()
b=Bee()

d.voice()
c.voice()
b.voice()
#1. Создать от него три класса наследника и для каждого сделать свою реализацию метода voice().

#2. Создать по одному экземпляру всех наследников и вызвать для каждого переопределенный метод voice().