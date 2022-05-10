class Human:
    life = 100
    endurance = 100
    height = 175
    development = 100
    def __init__(self):
        print("Human")
        print("\tlife",self.life)
        print("\tendurance", self.endurance)
        print("\theight", self.height)
        print("\tdevelopment", self.development)
class Goblin(Human):
    life = 50
    endurance = 150
    height = 75
    development = 45
    сunning = 100
    def __init__(self):
        print("Goblin")
        print("\tlife",self.life)
        print("\tendurance", self.endurance)
        print("\theight", self.height)
        print("\tdevelopment", self.development)
        print("\tсunning", self.сunning)
class Ogr(Human):
    life = 150
    endurance = 50
    height = 250
    development = 0
    strong = 200
    def __init__(self):
        print("Ogr")
        print("\tlife",self.life)
        print("\tendurance", self.endurance)
        print("\theight", self.height)
        print("\tdevelopment", self.development)
        print("\tstrong", self.strong)
class Magician(Human):
    magic = 100
    def __init__(self):
        print("Magician")
        print("\tlife",self.life)
        print("\tendurance", self.endurance)
        print("\theight", self.height)
        print("\tdevelopment", self.development)
        print("\tmagic",self.magic)
Sasha = Human()
Temharyak = Goblin()
Org = Ogr()
Naky = Magician()