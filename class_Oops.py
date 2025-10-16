class car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.is_started=False
    def start(self):
        if not self.is_started:
            print(f"The {self.year} {self.make} {self.model} is starting")
            self.is_started=True
        else:
            print(f"The {self.year} {self.make} {self.model} is already runnig")
    def stop(self):
        if self.is_started:
            print(f"The {self.year} {self.make} {self.model} is stopping")
            self.is_started=False
        else:
            print(f"The {self.year} {self.make} {self.model} is already stopped")

my_car=car("Hyndai","Alcazar",2024)
print(f"My car:{my_car.make} {my_car.model} ({my_car.year})")
my_car.start()
my_car.start()
my_car.stop()
my_car.stop()
