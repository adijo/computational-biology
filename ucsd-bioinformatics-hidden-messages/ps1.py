def count(genome, seq):
	if len(genome) < 3:
		return 0
	else:
		if genome[:3] == seq:
			return 1 + count(genome[1:], seq)
		else:
			return count(genome[1:], seq)

def freq_3mer(seq):
	d = {}
	for i in range(len(seq) - 3):
		small = seq[i : i + 3]
		if small in d:
			d[small] += 1
		else:
			d[small] = 1
	return max(d.keys(), key = lambda x : d[x])


def reverse_complement(seq):
	transform = {
		"A" : "T",
		"T" : "A", 
		"C" : "G",
		"G" : "C"
	}
	return ''.join(map(lambda x : transform[x], list(seq)))[::-1]

print reverse_complement("CCAGATC")

