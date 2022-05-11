

# class Computer:
#     def __init__(self,model,*args,**kwargs):
#         super().__init__(*args, **kwargs)
#         self.model = model
#         self.memory = 128
#     def calculate(self):
#         print("Calculating...")
# class Display:
#     def __init__(self,*args,**kwargs):
#         super().__init__(*args,**kwargs)
#         self.resolution = "4k"
#     def display(self):
#         print("I display the image on the screen...")
# class Phone:
#     def call(self):
#         print("calling...")
# class SmartPhon(Display,Computer,Phone):
#     def printInfo(self):
#         print(self.model)
#         print(self.memory)
#         print(self.resolution)
# iphone = SmartPhon(model = "Last")
# iphone.printInfo()


# class Class1:
#     var = 20
#     def __init__(self):
#         self.var = 10
# class Class2(Class1):
#     def __init__(self):
#         print(self.var)
#         super().__init__()
#         print(self.var)
#         print(super().var)
# obj = Class2()


# class Hello:
#     def __init__(self):
#         print("Hello")
# class HelloWorld(Hello):
#     def __init__(self):
#         super().__init__()
#         print("World")
# helW = HelloWorld()
