# WRITE YOUR SOLUTION HERE:
class Present:
    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight
    
    def __str__(self):
        return f"{self.name} Book ({self.weight} kg)"
    
class Box:
    def __init__(self):
        self.weight_total = 0

    def add_present(self, p: "Present"):
        self.weight_total += p.weight

    def total_weight(self): 
        return self.weight_total



if __name__ == "__main__":
    book = Present("ABC Book", 2)

    box = Box()
    box.add_present(book)
    print(box.total_weight())

    cd = Present("Pink Floyd: Dark Side of the Moon", 1)
    box.add_present(cd)
    print(box.total_weight())