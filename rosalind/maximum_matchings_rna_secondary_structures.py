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
g = 0
u = 0
for char in genome:
    if char == "A":
        a += 1
    elif char == "U":
        u += 1
    elif char == "G":
        g += 1
    else:
        c += 1

def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))

first = factorial(max(a, u)) / factorial(max(a, u) - min(a, u))
second = factorial(max(g, c)) / factorial(max(g, c) - min(g, c))


print first * second