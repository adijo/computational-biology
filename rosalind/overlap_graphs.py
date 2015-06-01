import sys

in_file = sys.argv[1]

f = open(in_file, "r")


graph = {}
info = {}
K = 3 # problem asks for O_3 graph.

while True:
    identifier = f.readline().strip()
    dna = f.readline().strip()
    dna2 = f.readline().strip()
    dna = dna + dna2
    if not dna or not identifier: break
    graph[identifier[1:]] = []
    info[identifier[1:]] = dna

def edge(this, that):
    if this[len(this) - K:] == that[:K]:
        return True
    else:
        return False

for this in graph:
    for that in graph:
        if this != that:
            if edge(info[this], info[that]):
                graph[this].append(that)

for node in graph:
    for value in graph[node]:
        print node, value