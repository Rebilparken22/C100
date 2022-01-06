class Car:

    #constructor
    def __init__(self,model,brand,cost):
        self.model = model
        self.brand = brand
        self.cost = cost

    def describe(self):
        print("this car is the newest", self.brand,self.model,". It costs",self.cost)    

car1 = Car("C1","peugeot","£3000")
car2 = Car("Zonda","pagani","£350000")
car3 = Car("Aventador","Lamborgini","£250420")
car4 = Car("C1","peugeot","£3000")
Car.describe(car1)