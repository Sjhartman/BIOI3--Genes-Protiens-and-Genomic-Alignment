# BIOI3--Genes-Protiens-and-Genomic-Alignment
Series of python files used to complete the third course of Coursera's Bioinformatics Specialization from UC San Diego

1 The minimum coins algorithm provides the foundation for sequence alignment algorithms to rapidly find the most matches and minimum indels/mismatches between two sequences

2 The "Manhattan Tourist Problem" takes weighted directed acyclic graphs (Grid format) to find the longest path starting from the top left of the grid to the lower right, utilizing dynamic programing to run in O(n*m) time

3 Longest Path Directed Acyclic graph finds the longest path of interest between two sepcific nodes rather than longest path in the entire graph

4 Longest Path Test Case - example input/output for Longest Path Directed Acyclic graph

5 Blosum62 Matrix: Matrix used for penalizing mismatches in sequence alignments, and match scores between matching residues

6 Penalized Sequence Alignment: Uses the Blosum62 penalty matrix for determining the highest scoring paths within each sequence alignment. The input are two amino acid strings, with each amino acid reprented as a 1 letter code

7 Local sequence alignment: Finds highest scoring local alignment by repositioning source and sink nodes to optimize longest path scores while generating the alignment matrix.

8 Linearspace sequence alignments: Divide and conquer strategy for performing the global sequence alignment with linear memory in O(nm). The alignment matrix is recursively divided into smaller matrices until every middle edge can be concatenated to produce the longest path and generate a global sequence alignmnet.

9 Primitive multiple sequence alignment. Practices using a 3 dimensional path to map the longest path between 3 sequences. Uses dynamic programing and a backtrack dictionary to trace the path for each line of the alignment.
 
10 Synteny Match with Greedy Algorithm: Attempts to align to genomes using a greedy algorithm that rearranges chromosomes based on their desired index and orientation. This model is not likely to be evolutionarily relevant as it does not produce the shortest path

11 Breakpoint Graphs: Aligns two genomes to find 'breakpoints' or areas of synteny blocks that should be re-arranged to produce one genome from another. This strategy is more evolutionarily relevant than the greedy strategy, because it finds the shortest number of steps to transform one genome into another. However, there are multiple paths to transform the genomes into eachother that have the same amount of steps. 
