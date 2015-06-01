import sys

in_file = sys.argv[1]

f = open(in_file, "r")
line = f.readline().strip()

codon_table = {
    
    'F' : 2,
    'L' : 6,
    'S' : 6,
    'Y' : 2,
    'C' : 2,
    'W' : 1,
    'P' : 4,
    'H' : 2,
    'Q' : 2,
    'R' : 6,
    'I' : 3,
    'M' : 1,
    'T' : 4,
    'N' : 2,
    'K' : 2,
    'V' : 4,
    'A' : 4,
    'D' : 2,
    'E' : 2,
    'G' : 4
}

answer = 1
for char in line:
    answer = (answer * codon_table[char]) % 1000000

answer = (answer * 3) % 1000000

print answer