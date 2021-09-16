class car:
    def __init__(self,gears,seats,maxSpeed):
        self.gears=gears
        self.seats=seats
        self.maxSpeed=maxSpeed

    def speedup(self):
        print("Speed Increasing")

    def applybreak(self):
        print("Speed Decreasing")

class Harrier(car): #Inheritance
    def __init__(self,mileage,gears,seats,maxSpeed):
        self.mileage=mileage
        super().__init__(gears,seats,maxSpeed) #We want mileage attribute too, so we are overridding init method and using super keyword

    def race_mode(self):
        print("Race mode is on")

c1=car(5,6,250)
h1=Harrier(5,4,240)
print(h1.gears)
print(h1.seats)
print(h1.maxSpeed)
h1.speedup()
h1.applybreak()
h1.race_mode()
