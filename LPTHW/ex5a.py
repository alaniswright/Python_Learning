name = 'Zed A. Shaw'
age = 35 # not a lie
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

# Height
height_in_inches = 74
inches_to_cm = 2.54
height = height_in_inches * inches_to_cm # height in cm

#Weight
weight_in_lbs = 180
lbs_to_kg = 0.4536
weight = weight_in_lbs * lbs_to_kg # weight in kg


print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually, that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
