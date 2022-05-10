# class Student:
#     studentsCount = 0
#     def __init__(self,name,progress,db,school):
#         self.name = name
#         self.progress = progress
#         self.dateofBirthday = db
#         self.school = school
#         Student.studentsCount += 1
#     def __str__(self):
#         return f"№{self.studentsCount} \n name: {self.name} \n progress: {self.progress} \n dateofBirthday: {self.dateofBirthday}"
#     def addProgress(self, a):
#         self.progress += a
#         print("Student mark:",self.progress)
#     def method(self):
#         print("method")
# class Auto():
#     def __init__(self,brand):
#       self.brand = brand
#       self.passengers = []
# def (self, human):
#     self.passengers.append(human)
class Soda:
    def __init__(self, supplements = str(input("input supplements in soda: "))):
        self.supplements = supplements
    def show_my_drink(self):
        if self.supplements != "":
            print(f"Газована вода з {self.supplements}")
        else:
            print(f"Звичайна газована вода")
soda = Soda()
soda.show_my_drink()


#object = Student("object",10, "04.05.2007",17)
#print(object)
#James = Student("James",9, "13.12.2006",17)
#print(James)
#Robert = Student("Robert",11, "26.05.2007",17)
# print(Robert)
# Robert.addProgress(int(-2))

