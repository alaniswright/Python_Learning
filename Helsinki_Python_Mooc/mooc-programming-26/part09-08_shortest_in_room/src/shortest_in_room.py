# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.persons = []

    def add(self, person):
        self.persons.append(person)

    def is_empty(self):
        if len(self.persons) == 0:
            return True
        else:
            return False

    def print_contents(self):
        height = 0
        text2 = ""
        for p in self.persons:
            text2 += f"{p.name} ({p.height} cm)\n"
            height += p.height
        text1 = f"There are 5 persons in the room, and their combined height is {height} cm\n"
        text = text1 + text2
        print(text)

    def shortest(self):
        if self.is_empty():
            return None
        else:
            shortest = self.persons[0]
            for person in self.persons:
                if person.height < shortest.height:
                    shortest = person
            return shortest
    
    def remove_shortest(self):
        if self.is_empty():
            None
        else:
            v = self.shortest()
            self.persons.remove(v)
            return v


if __name__ == "__main__":
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()