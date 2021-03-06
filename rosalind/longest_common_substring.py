def longest_substring(a, b):
    dp = {}
    # dp[(i, j)] indicates the longest common substring 
    # of a and b ending at indices i and j.
    for i in xrange(len(b)):
        if a[0] == b[i]:
            dp[(0, i)] = 1
        else:
            dp[(0, i)] = 0
    for i in xrange(len(a)):
        if a[i] == b[0]:
            dp[(i, 0)] = 1
        else:
            dp[(i, 0)] = 0

    for i in xrange(1, len(a)):
        for j in xrange(1, len(b)):
            if a[i] == b[j]:
                dp[(i, j)] = dp[(i - 1, j - 1)] + 1
            else:
                dp[(i, j)] = 0
    string = None
    maximum = 0
    for key in dp:
        if dp[key] > maximum:
            maximum = dp[key]
            string = a[key[0] - maximum + 1: key[0] + 1]
    return string


a = """GCAACGTCTCCAGCCACAGCGCATCAAGGTTGCGGTTAGCCCGAGTTCCAGCGTCGAGTTCCTACAGTCTGAAAAAATCTATATTCAGCTACGTATGCTCAGATAACGAGCGTCCTGCATAGGGTTGTCGCAAGCGTGTTAATGCCCCCTATGCCGTTGTCCCAAGTACTAACTCGCAGAACTCGGAGGGGGAAGCAAAAGGTGGCACGGATGCGTATTTAGTCTCCATGCTGAGTTAGTACTAGTAAAAGAGAGTACTTGCATGACCTATCATTGAATAAGACGGGATCTCTCGGCAGGTCTCTAGTGCAGCTATTTCCCATGTCATAGGGAATTTTTTTGCTGGTAACCCGCGCATTAGCAATTATATCCGTGGTAGTTTTTGCAGGGCGCCGCTCGCGGACCCTAGCAGAGGTTCCGAGTAGTAATAAGGTGGGAAAATGTTCAAGATGAGCTGAATGTACTATGTCCACCACCGACGGCTCTGCATTAATTAAGTGGTTCCCTTAGCAGGAACTGCTACCATGTACGTATTTCAGCTTAGTATTCTAGTACCGAAGTTAACGGTGGATTATTGACGTGCTCGTCACCCGAGTTAAGCGATCGTACTCAACCGACCAACGCGAGCTTTGCTAAATCATCTCGGAGGAACCGTCACGTTTTTAGAGACCGTTTTAAGGCAAGGGTATTGAAGAGCAGGTGCTCAATGGTAGTAGTATGTACATGTTGATGTAGCTTGTCCCAAGAATACTCGGACGACCACTTCTGGGCTCATTGGCGTGGAAAACCGGGGGCGCTTTAGCATGTAAGTTCCTTTTGAACCCTGGTGGGTATCCTGGGTCCCGTGGTAGTGGTCTTGGTGCAAATATGTCAAACCATCTCAGACTGTTACGATCCACCTCGATTGATCAGTGCCCGAGAGAGTCTACCGGGATCGTGTCTGAGATCAATCACCCGATCTAACACGGCACCTTCGTGGAAAGGTTTGCATCATACACCG"""
b = """GCGCCAATTGTATGCGGAAGTAATGACATCGATCCGTCCAGTGCAAGATTGCTACACTTTTACGTACATAAGTCTATGAGCAAATAGGGCATTTGGCAGTGGAAGCGGTTATGGCCTGCATAGTTTTATGTTTAAGCCCTTAGACATCCTAAGCTGCAAGGCCGAGATTTATCTCTCCAGCCCTCGATGAAGCACACTGCTGCAACGGGACCCGCCACAAACGGTGGTCGTTACTGTTTATTCTAGATTTCTATCGCTTATGGCCTAGCAGAGAGTCCCTGGAGTATTTTGGTGTTAAATCTTTTGGGTTGGCAGGATACGGTTCTATATAGACTAGCCGTGCCCTCGTGAGGAGCAGAACCGTCCTGATTAGAACTAGACACTAGGTCGGACCACGGCACGGGTACGGTGCTATGTTTATCTACCCGCCAGGTCCATTGGTTAGACTATATCACAACTGTGGCCTGACATTCTTAAGCATCGCCGCATTGTCTCTATTATAATACGATATGATCTTGTACTCAGTGCCAGGATATGAGTTGCTACTACTTTTGAGGGCTCCAGAAGTACATAGTTCATTTTTGTTCGCGAGAGTTCCGCTTCGGTTATAAACTGCTGCTGTTATGTCGCCAATATTTCCTGACCCAGAAATACAGCTTGTGCCGGTGTTGCCTCATCTGCGGTCTTTCACAGGGTACCTCGACACCGTCTGAGAAACTATTGGCACTGTCTCTAGCTTATCGCATAAGTTCGCCTTGCAGAAGCCTTGTGTCTCCCTGGTCTAAATCTAATCCCAAGTGTTACACGATGCTAAGGTCCAATCGGTACGCTAGAACTGGACAATAGGCCTTGAGCAGCCACTACGAGTGCCGATCGTGTCCCGGCAATGTCCTTCTTGGGGAATGAACAAGCTGTGACTTCCGTATGTTTTCAGGGTTGCCGGCGTGTGCGACCGCATGGGAAAAGCGATGAAACGTACATCTGGGGGAGGAGAGCTTGC"""

print longest_substring(a, b)