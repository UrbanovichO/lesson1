class TV:
    def __init__(self,year,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.year = year
        self.model = 12
    def display(self):
        print("I displaing")
class tablet:
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.memory = 64
    def BownloadMusic(self):
        print("I downloading music")
class NoteBook:
    def PlayGame(self):
        print("I play game")
class Phone:
    def calculate(self):
       print("I calculating")
class Computer(TV,tablet,NoteBook):
    def PrintInfo(self):
        print("Computer")
        print("\tYear",self.year)
        print("\tMemory",self.memory,"GB")
        print("\tModel",self.model)
Intel = Computer(year = 2020)
Intel.PrintInfo()

