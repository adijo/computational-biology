import sys, math

in_file = sys.argv[1]

f = open(in_file, "r")

f.readline()
genome = []
while True:
    l = f.readline()
    if not l:
        break
    genome.append(l.strip())

genome = ''.join(genome)
a = 0
c = 0
for nucleotide in genome:
    if nucleotide == 'A':
        a += 1
    if nucleotide == 'C':
        c += 1

def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))

print factorial(a) * factorial(c)