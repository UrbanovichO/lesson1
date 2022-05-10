# class Human:
#     weight = 70
#     old = 80
#     endurance = 100
#     def __init__(self):
#         print("Human")
#         print("\tweight",self.weight)
#         print("\told",self.old)
#         print("\tendurance",self.endurance)
# class Elves(Human):
#     weight = 55
#     old = 500
#     endurance = 897
#     manna = 45
#     def __init__(self):
#         print("Elves")
#         print("\tweight", self.weight)
#         print("\told", self.old)
#         print("\tendurance", self.endurance)
#         print("\tmanna",self.manna)
# class Hobbyt(Human):
#     weight = 25
#     endurance = 50
#     def __init__(self):
#         print("Hobbyt")
#         print("\tweight", self.weight)
#         print("\told", self.old)
#         print("\tendurance", self.endurance)
# a = Human()
# b = Elves()
# c = Hobbyt()

# class Human:
#     height = 170
# class Student(Human):
#     mark = 5
#     pass
# class Worker(Student):
#     salary = 120
#     pass
# nick = Student()
# ann = Worker()
# print("Nick height",nick.height)
# print("Ann height",ann.height)
# print(nick.mark)
# print(ann.mark)

class Hello_world:
    hello = "Hello"
    _hello = "_Hello"
    __hello = "__Hello"

    def __init__(self):
        self.world = "World"
        self._world = "_World"
        self.__world = "__World"

    def printer(self):
        print(self.hello)
        print(self._hello)
        print(self.__hello)
        print(self.world)
        print(self._world)
        print(self.__world)


class Hi(Hello_world):

    def hi_print(self):
        print(self.hello)
        print(self.world)
        print(self._hello)
        print(self._world)
        print(self._Hello_world__hello)
        print(self._Hello_world__world)
        hello = Hello_world()
        hello.printer()


hi = Hi()
hi.hi_print()

# class Human:
#     height = 170
# class Student(Human):
#     mark = 5
#     pass
# class Worker(Human):
#     salary = 120
#     pass
# nick = Student()
# ann = Worker()
# print("Nick height",nick.height)
# print("Ann height",ann.height)
# print(nick.mark)
# print(ann.salary)

