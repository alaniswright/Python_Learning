# Write your solution here
def create_tuple(x: int, y: int, z: int):
    l = [x, y, z]
    return (min(l), max(l), sum(l))