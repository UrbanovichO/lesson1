class Soda:
    def __init__(self, supplements = input("input supplements in soda: ")):
        self.supplements = supplements
    def show_my_drink(self):
        if self.supplements != "":
            print(f"Газована вода з {soda.supplements}")
        else:
            print("Звичайна газована вода")
soda = Soda()
soda.show_my_drink()
