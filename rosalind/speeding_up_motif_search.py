"""
Calculates the prefix table of a pattern.

The prefix table denotes for the substring from [0 ... i], 
the length of the longest proper prefix and proper suffix 
of that substring.

"""


def prefix_table(string):
    table = [0] * len(string)
    j = 0
    for i in xrange(1, len(string)):
        if string[i] == string[j]:
            table[i] = j + 1
            j += 1
        else:
            while j > 0 and string[i] != string[j]:
                j = table[j - 1]
            if string[j] == string[i]:
                table[i] = j + 1
                j += 1
    return table
