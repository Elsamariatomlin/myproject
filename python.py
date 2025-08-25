# class Animal:
#     def speak(self):
#         print("Animal speaks")

# class Dog(Animal):
#     def speak(self):
#         print("Dog barks")  # Overrides parent method

# Dog().speak()  # Output: Dog barks



class Fruits:
    def taste(self):
        print("fruits are sweet")
    def __init__(self,name,color,shape):
        self.name=name
        self.color=color
        self.shape=shape
    def details(self):
          print(f"the name of the fruit is {self.name} and the color is {self.color} and the shape is {self.shape}")
class mango(Fruits):
    def __init__(self,name,color,shape,price):
        super().__init__(name,color,shape)
        self.price=price
    def display(self):
            print(f"the price of the mango is {self.price}")
f1=mango("mango","green","round",100)
f1.details()
f1.display()
f2=mango("mango","yellow","round",130)
f2.details()
f2.display()