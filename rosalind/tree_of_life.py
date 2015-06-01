import sys

in_file = sys.argv[1]

f = open(in_file, "r")

n = int(f.readline().strip())
ctr = 0
while True:
	line = f.readline()
	if not line:
		break
	else:
		ctr += 1

print n - ctr - 1