class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("запуск отрисовки")

class Pen(Stationery):
    def draw(self):
        print(f"Отрисовка ручкой {self.title}")

class Pencil(Stationery):
    def draw(self):
        print(f"отрисовка карандашом {self.title}")

class Handle(Stationery):
    def draw(self):
        print(f"отрисовка маркером {self.title}")

item_1 = Stationery("")
item_2 = Pen("(черные чернила)")
item_3 = Pencil("(простой карандаш)")
item_4 = Handle("(красный цвет)")

item_1.draw()
item_2.draw()
item_3.draw()
item_4.draw()
