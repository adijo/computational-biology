import operator as op


def ncr(n, r):
    r = min(r, n - r)
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n - r, -1))
    denom = reduce(op.mul, xrange(1, r + 1))
    return numer // denom


k, n = map(int, raw_input().split())

acc = 0

# changing these variable names to make it clear to read.
# N = 2^k = total number of organisms at the kth level.
# K equals to the number of 'successes'

N = pow(2, k)
K = n

for i in xrange(K, N + 1):
    combinations = ncr(N, i)
    success = pow(0.25, i)
    failure = pow(0.75, N - i)
    acc += (combinations * success * failure)

print round(acc, 3)

<script src="https://gist.github.com/adijo/dcb12f1dcc9c24bdf8db.js"></script>