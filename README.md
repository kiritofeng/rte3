All test cases are fetched from the
[SNAP datasets](https://snap.stanford.edu/data/index.html).

## Input File Format

The input format is the `.edges` format: the first line contains two
space-separated integers, *N* and *M*, indicating that the graph has *N*
vertices and *M* edges.

The next *M* lines contain two space-separated integers, *u* and *v*, indicating
there is an undirected edge connecting vertices *u* and *v*. These vertices are
0-indexed.

## Output File Format

The output file lists the number of *k*-cliques in the graph, starting from *k*=3
and ending with the number of cliques of maximal size.
