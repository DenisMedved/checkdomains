
import sys
import itertools
from itertools import product
from string import ascii_lowercase

if len(sys.argv) < 2:
    print(sys.exit("Filename with domains as as first argiment is requered"))

filepath = sys.argv[1]

with open(filepath, "w") as f:
    for letters in range(2, 4):
        for i in product(ascii_lowercase, repeat = letters):
            f.write("".join(i) + "\n")

print("Done");