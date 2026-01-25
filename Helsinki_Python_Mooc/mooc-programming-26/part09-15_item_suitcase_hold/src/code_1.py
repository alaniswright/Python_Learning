# Write your solution here:
class Item:
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight
    
    def weight(self):
        return self.__weight
    
    def name(self):
        return self.__name
    
    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"
    
class Suitcase:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__items = []
    
    def weight(self) -> int: 
        total = 0
        for item in self.__items:
            total += item.weight()
        return total
    
    def add_item(self, item: "Item"):
        if (self.weight() + item.weight()) <= self.__max_weight:
            self.__items.append(item)
    
    def __str__(self):
        i = "items"
        if len(self.__items) == 1:
            i = "item"
        return f"{len(self.__items)} {i} ({self.weight()} kg)"

    def print_items(self):
        for item in self.__items:
            print(item)
    
    def heaviest_item(self):
        heavy_item = self.__items[0]
        heavy_item_weight = self.__items[0].weight()
        for item in self.__items:
            if item.weight() > heavy_item_weight:
                heavy_item = item
                heavy_item_weight = item.weight()
        return heavy_item
    
class CargoHold:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__items = []
    
    def weight(self):
        weight = 0
        for suitcase in self.__items:
            weight += suitcase.weight()
        return weight
    
    def add_suitcase(self, suitcase: "Suitcase"):
        if self.weight() + suitcase.weight() <= self.__max_weight:
            self.__items.append(suitcase)
    
    def __str__(self):
        i = "suitcases"
        if len(self.__items) == 1:
            i = "suitcase"
        return f"{len(self.__items)} {i}, space for {self.__max_weight - self.weight()} kg"

    def print_items(self):
        for suitcase in self.__items:
            suitcase.print_items()



if __name__ == "__main__":
    suitcase = Suitcase(25)
    item1 = Item("ABC Book", 2)
    suitcase.add_item(item1)
    item2 = Item("Hammer", 10)
    suitcase.add_item(item2)
    item3 = Item("Rock", 3)
    suitcase.add_item(item3)
    print(suitcase.heaviest_item())