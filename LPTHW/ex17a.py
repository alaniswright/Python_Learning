from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
in_file = open(from_file, 'r').read()
#indata = in_file.read()

print(f"The input file is {len(in_file)} bytes long")

if exists(to_file) == True:
    out_file = open(to_file, 'w').write(in_file)
    #out_file.write(in_file)
    print("Alright, all done.")
    #out_file.close()

else:
    print("Output file does not exist.")
#print(f"Does the output file exist? {exists(to_file)}")
#print("Ready, hit RETURN to continue, CTRL-C to abort.")
#input()




#python ex17a.py test1.txt test2.txt
