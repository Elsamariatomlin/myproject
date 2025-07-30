class vehicle:
    def __init__(self,name,color,price):
        self.name=name
        self.color=color
        self.price=price
    def details(self):
        print(f"name:{self.name},color:{self.color},price:{self.price}")

class car(vehicle):
    def __init__(self, name, color, price,speed):
        super().__init__(name, color, price)
        self.speed=speed
    def car_details(self):
            super().details()
            print(f"speed:{self.speed}")
car1=car("xuv","blue",249000,120)
car1.car_details()