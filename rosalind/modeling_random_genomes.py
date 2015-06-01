import sys, math

in_file = sys.argv[1]

f = open(in_file, "r")

genome = f.readline().strip()
gc_content = [float(x) for x in f.readline().strip().split()]


def log_probability(at, gc):
	acc = 0
	for nucleotide in genome:
		if nucleotide == 'A' or nucleotide == 'T':
			acc += math.log(at, 10)
		else:
			acc += math.log(gc, 10)
	return str(acc)

answer = []
for content in gc_content:
	gc = content / 2.0
	at = (1 - content) / 2.0
	answer.append(log_probability(at, gc))

print ' '.join(answer)
