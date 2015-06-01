import sys

in_file = sys.argv[1]

f = open(in_file, "r")
line = f.readline().strip()

genotype_to_offspring = {0 : 2, 1 : 2, 2 : 2, 3 : 1.5, 4 : 1, 5 : 0}

samples = map(int, line.split())
print sum(map(lambda x : samples[x] * genotype_to_offspring[x], range(len(samples))))