def show_names(names):
    for name in names:
        print(name)

def make_names_great(names):
   for i in range(len(names)):
        names[i] = names[i] + " the great"
   return names