class UnderwaterCreature:
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

    def describe(self):
        return f"{self.name} libes in the {self.habitat}."


class Orca(UnderwaterCreature):
    def __init__(self, name, habitat, lenght):
        super(), __init__(name, habitat) #common attributes name and habitat, common method describe
        self.lenght = lenght

        def describe(self):
            return f"{self.name} is an Orca that is {self.length} meters long and lives in the {self.habitat}. They are known for their intelligence and complex social structure."


class Clownfish(UnderwaterCreature): #each subclass inherits using the super() funct, but adds unique attr, each subclass ovverrides describe method
    def __init__(self, name, habitat, species):
        super(), __init__(name, habitat) #common attributes name and habitat, common method describe
        self.species = species

    def describe(self):
        return f"{self.name} is a {self.species}, it lives in the {self.habitat}."


class Eel(UnderwaterCreature):
    def __init__(self, name, habitat, lenght, wrong_species,correct_species, electric):
        super(), __init__(name, habitat) #is to call methods and access attributes from the parent class within a subclass
        self.electric = electric
        self.lenght = lenght
        self.wrong_species = wrong_species
        self.correct_species = correct_species

    def describe(self):
        return f"{self.name} is a not {self.wrong_species}, but a {correct_species}. It lives in the {self.habitat}. It is {self.lenght} meters long and is {self.electric}."


class Shark(UnderwaterCreature):
    def __init__(self, name, habitat, lenght):
        super(), __init__(name, habitat)
        self.lenght = lenght

    def describe(self):
        return f"{self.name} is a viper shark that lives in the {self.habitat} and is {self.lenght} meters long."


orca = Orca("Orcinus orca", )
nemo = Clownfish("Amphiprion ocellaris", "coral reefs of the Indian Ocean", "Clownfish")
eel = Eel("Anguilla japonica", "eel", "knifefisch")
shark = Shark("Electrophorus electricus", "Pacific Ocean")
