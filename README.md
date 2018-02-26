# Argparse_02.18
# Description
*A repository containing an argparse executable utility perforing a Needleman-Wunsch over two nucleotide sequences*

# Basic Idea
A Needleman-Wunsch algorithm is a **global alignment algorithm** that allows aligning two nucleotide or amino acid strings one against another thus defining both similarity score and positional matches in the resulting alignment. Compared strigs comprise two axis of a comparison grid, and the algorithm leads an imaginary maze-running trace from left upper corner down to right lower corner. By default, the grid s filled with zeros, but during the alignment resolving it is filled with match/mismatch/indel score, which results in the left lower cell's final alignment score. The aim of the algorithm is to find the minimal score 'way' which stands for most parsinimous alignment.


# Structure

## Code Summary

The program is written in Python3.6 and contains a Needleman-Wunsch algorithm function and a terminal executor.

## Input Syntax

The program launches by its default file name with three arguments:
- s1: a nucleotide string variable of python class 'str'; default is 'CCC';
- s2: a nucleotide string variable of python class 'str'; default is 'GGGG';
- g: an indel penalty variable of python class 'int'; default is 5.

## Performance

The Needleman-Wunsch function falls into three conventional parts:

1. *Sequence definer*: assigns two input sequences to seq1 and seq2 variables as well as their lengths to n and m variables

```
if len(seq1) < len(seq2):
    seq1, seq2 = seq2, seq1
    n, m = len(seq2), len(seq1)
```

2. *Grid builder*: creates a numpy zero array of n by m size and fills it with match and indel values:

```
for i in range(1, m + 1):
    Wmin[0][i] = Wmin[0][i - 1] + g
for j in range(1, n + 1):
    Wmin[j][0] = Wmin[0][j - 1] + g
```

3. *Grid runner*: resolves the grid by finding the shortest path from right upper to left lower corner:

```
for i in range(1,n + 1):
    for j in range(1, m + 1):
        deletion = Wmin[i][j - 1] + g
        insertion = Wmin[i - 1][j] + g
        match = Wmin[i - 1][j - 1] + int(seq1[j-1]!=seq2[i-1])
        Wmin[i][j] = max(deletion, insertion, match)
```

The function returns a final score value which corresponds to nm cell of the grid.

# Important Notes
Apart from argparse library, the program also requires numpy library for eased array building.
Default indel penalty is arbitrarily set as 5 which is by far the most common gap value found in the minimal score alignment algorithms. Note that is an input argument and can be set according to your needs and preferences.

# Acknowledgements
Eugene Bakin from Bioinformatic Institute for Python crash course.

[Python for Beginners](http://www.pythonforbeginners.com/argparse/argparse-tutorial) for its useful Argparse guide.
