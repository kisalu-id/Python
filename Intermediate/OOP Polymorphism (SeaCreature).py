class SeaCreature: #base class that contains methods
    def intro(self):
        print("I'll tell a little about different sea creatures.")

    def speed(self):
        print("They can move at different speeds.")


class Orca(SeaCreature):
    def intro(self): #even if the methodes are inherited, they're unique => polymorphism
        print("This is an Orca, also known as a killer whale. Orcas are highly intelligent and social creatures.")

    def speed(self):
        print("An Orca can swim at speeds up to 56 km/h.")

class Octopus(SeaCreature):
    def intro(self):
        print("This is an Octopus, known for its intelligence, ability to camouflage, and it hass eight arms.")

    def speed(self):
        print("An Octopus can move at speeds up to 40 km/h, but usually they move much slower.")

class Eel(SeaCreature):
    def intro(self):
        print("This is an Eel, a long, snake-like fish often found in both fresh and saltwater environments.")

    def speed(self):
        print("An Eel can swim at speeds up to 24 km/h.")

class Jellyfish(SeaCreature):
    def intro(self):
        print("This is a Jellyfish, known for its gelatinous body and tentacles that can deliver stings.")

    def speed(self):
        print("A Jellyfish moves by pulsating its bell, generally at speeds around 8 km/h.")

 
sea_creatures = [Orca(), Octopus(), Eel(), Jellyfish()]

for creature in sea_creatures:
    creature.intro()
    creature.speed()
    print()

#polymorphism means that you can use  a common method on different objects, and each object can respond in its own way
