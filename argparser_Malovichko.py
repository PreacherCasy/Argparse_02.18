import numpy as np
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Whatever')
    parser.add_argument('-s1', help='Enter sequence 1', metavar = 'Str', type = str, default='CCC' )
    parser.add_argument('-s2', help='Enter sequence 2', metavar = 'Str', type = str, default='GGGG' )
    parser.add_argument('-g', help='Gap penalty', metavar = 'Int', type = int, default = 5 )
    args = parser.parse_args()
    seq1 = args.s1
    seq2 = args.s2
    g = args.g
def NeedlemanWunsch(seq1, seq2, g):
    if len(seq1) < len(seq2):
        seq1, seq2 = seq2, seq1
    n, m = len(seq2), len(seq1)
    Wmin = np.zeros((n + 1, m + 1))
    for i in range(1, m + 1):
        Wmin[0][i] = Wmin[0][i - 1] + g
    for j in range(1, n + 1):
        Wmin[j][0] = Wmin[0][j - 1] + g
    for i in range(1,n + 1):
        for j in range(1, m + 1):
            deletion = Wmin[i][j - 1] + g
            insertion = Wmin[i - 1][j] + g
            match = Wmin[i - 1][j - 1] + int(seq1[j-1]!=seq2[i-1])
            Wmin[i][j] = max(deletion, insertion, match)
    return(Wmin[n][m])
print(NeedlemanWunsch(seq1, seq2, g))