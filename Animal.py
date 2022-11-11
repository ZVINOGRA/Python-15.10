class Animal:
    def __init__(self, name, space):
        self.name = name
        self.space = space

    def __str__(self):
        return self.name


class Cage:
    def __init__(self, space, animal_list):
        self.space = space
        self.animal_list = animal_list

    def add_animal(self, animal: Animal):
        if self.space >= animal.space:
            print(True)
            self.space -= animal.space
            self.animal_list.append(animal.name)
        else:
            print(False)

    def get_animals(self):
        return self.animal_list

    def free_space(self):
        return self.space


cage1 = Cage(300, [])
cage2 = Cage(200, [])

lion = Animal("Alex", 150)
pinguin1 = Animal("Gunter", 20)
pinguin2 = Animal("Ganter", 15)
pinguin3 = Animal("Ginter", 25)
begemoth = Animal("Gloria", 200)
giraffe = Animal("Melvin", 110)
zebra = Animal("Martin", 70)

print(cage1.add_animal(giraffe))
print(cage1.add_animal(begemoth))
print(cage2.add_animal(zebra))
print(cage2.free_space())
print(cage1.get_animals())