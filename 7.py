#Необходимо дополнить "Практическое задание №6" таким образом, чтобы в конце программы мы вызвали
#статический метод родительского класса Animal, который вывел бы нам количество всех созданных экземпляров.
#Если мы создали трех наследников в предыдущем задании, то наш метод должен вывести на экран число 3
class Animal:
    num_of_insts = 0

    def __init__(self):
        Animal.num_of_insts = Animal.num_of_insts + 1

    def print_num():
        print(Animal.num_of_insts)

    print_num = staticmethod(print_num)

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

Animal.print_num()
