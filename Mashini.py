class Car:
    total_cars = 0

    def __init__(self,carmake, model, speed):
        self.carmake = carmake
        self.model = model
        self.speed = 0
        Car.total_cars += 1

    def speed_up(self, value):
        self.speed += value
        print(f"{self.carmake} {self.model} ускорятеся на {self.speed}")

    def speed_down(self, value):
        self.speed -= value
        print(f"{self.carmake} {self.model} приостанавливается на {self.speed}")

    @staticmethod
    def show_all_cars():
        return Car.total_cars

car_1 = Car("Lada", "Kalina", 10)
car_2 = Car("Rolls Royce", "Fantom", 50)
car_1.speed_up(20)
car_2.speed_down(15)
total_cars = Car.show_all_cars()
print(total_cars)

