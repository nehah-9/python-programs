class animal:
    def make_sound(self):
        raise NotImplementedError("subclass must implement abstract method")
class dog(animal):
    def make_sound(self):
        return "Woof!Woof!"
class cat(animal):
    def make_sound(self):
        return "Meoww!"
class bird(animal):
    def make_sound(self):
        return "Chirp!chirp!"
animals=[dog(),cat(),bird()]
for animal in animals:
    print(f"An animal makes sound:{animal.make_sound()}")
