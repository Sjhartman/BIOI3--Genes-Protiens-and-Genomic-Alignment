# BIOI3--Genes-Protiens-and-Genomic-Alignment
Series of python files used to complete the third course of Coursera's Bioinformatics Specialization from UC San Diego

1 The minimum coins algorithm provides the foundation for sequence alignment algorithms to rapidly find the most matches and minimum indels/mismatches between two sequences

2 The "Manhattan Tourist Problem" takes weighted directed acyclic graphs (Grid format) to find the longest path starting from the top left of the grid to the lower right, utilizing dynamic programing to run in O(n*m) time

3 Longest Path Directed Acyclic graph finds the longest path of interest between two sepcific nodes rather than longest path in the entire graph

4 Longest Path Test Case - example input/output for Longest Path Directed Acyclic graph

5 Blosum62 Matrix: Matrix used for penalizing mismatches in sequence alignments, and match scores between matching residues

6 Penalized Sequence Alignment: Uses the Blosum62 penalty matrix for determining the highest scoring paths within each sequence alignment. The input are two amino acid strings, with each amino acid reprented as a 1 letter code

7 Local sequence alignment: Finds highest scoring local alignment by repositioning source and sink nodes to optimize longest path scores while generating the alignment matrix.
