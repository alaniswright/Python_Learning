# Write your solution here:
class SuperHero:
    def __init__(self, name: str, superpowers: str):
        self.name = name
        self.superpowers = superpowers

    def __str__(self):
        return f'{self.name}, superpowers: {self.superpowers}'

class SuperGroup:
    def __init__(self, name: str, location: str):
        self._name = name
        self._location = location
        self._members = []
    
    def name(self):
        return self._name
    
    def location(self):
        return self._location
    
    def add_member(self, hero: SuperHero):
        self._members.append(hero)
    
    def print_group(self):
        text = ""
        text += f"{self.name()}, {self.location()}\n"
        text += "Members:\n"
        for hero in self._members:
            text += f"{hero.name}, superpowers: {hero.superpowers}\n"
        print(text)