import sys

in_file = sys.argv[1]

f = open(in_file, "r")

matrix = {}
alphabet = ['A', 'C', 'G', 'T']
f.readline()
while True:
    g = []
    first = f.readline().strip()
    if not first: break
    g.append(first)
    while first[0] != '>':
        first = f.readline().strip()
        if len(first) == 0: break
        elif first[0] != '>': g.append(first)
    genome = ''.join(g)
    if len(matrix) == 0:
        for x in xrange(len(genome)):
            matrix[x] = {'A' : 0, 'G' : 0, 'C' : 0, 'T' : 0}
            matrix[x][genome[x]] += 1
    else:
        for x in xrange(len(genome)):
            matrix[x][genome[x]] += 1


def construct_consensus(matrix):
    consensus = []
    for key in matrix:
        char = max(matrix[key].iterkeys(), key = lambda x : matrix[key][x])
        consensus.append(char)
    return ''.join(consensus)


print construct_consensus(matrix)

for char in alphabet:
    print "%s:" % char, " ".join([str(matrix[x][char]) for x in xrange(len(matrix))])