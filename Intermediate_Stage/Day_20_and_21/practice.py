# this practice is on class inheritance

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print('Inhale, exhale')


class Fish(Animal):
    def __init__(self):
        super().__init__()
        self.gills = 4

    def breathe(self):
        super().breathe()
        print(f'with my {self.gills} gills')

    def swim(self):
        print('doing this underwater')


animal = Animal()
print(animal.num_eyes)

animal.breathe()

fish = Fish()
print(fish.gills)

fish.breathe()

fish.swim()
