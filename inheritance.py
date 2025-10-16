class animal:
    def __init__(self,name):
        self.name=name
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")
class dog(animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed
    def bark(self):
        print(f"The {self.name} (a{self.breed}) barks:Woof! Woof!")
class cat(animal):
    def __init__(self,name,color):
        super().__init__(name)
        self.name=name
        self.color=color
    def meow(self):
        print(f"{self.name} (a{self.color}) cat meows: Meow!")
class bird(animal):
    def __init__(self,name,species):
        super().__init__(name)
        self.name=name
        self.species=species
    def fly(self):
        print(f"{self.name} (a{self.species}) is flying high!")
my_dog=dog("bobo","chihuahua")
my_cat=cat("meme","bobtail")
my_bird=bird("caca","crow")
my_dog.eat()
my_dog.bark()
my_dog.sleep()
my_cat.eat()
my_cat.meow()
my_cat.sleep()
my_bird.eat()
my_bird.fly()
my_bird.sleep()
