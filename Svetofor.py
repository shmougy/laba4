import time


class TrafficLight:
    def __init__(self):
        self.color = "red"

    def running(self):
        print("светофор работает ")

        while True:
            if self.color == "red":
                print("red")
                time.sleep(7)
                self.color = "yellow"

            if self.color == "yellow":
                print("yellow")
                time.sleep(2)
                self.color = "green"

            if self.color == "green":
                print("green")
                time.sleep(5)
                self.color = "red"

svetofor = TrafficLight()
svetofor.running()
