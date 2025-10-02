Forest Lucky Path Walker<br>

🌳 Project Overview<br>
This project implements a tree traversal algorithm to find all root-to-leaf paths in a binary tree where the sum of node values equals a given "lucky number". The solution uses Depth-First Search (DFS) with backtracking to efficiently explore all possible paths from root to leaf nodes.

Key Features:<br>
Tree Construction: Build binary tree from serialized input (supports 'null' for empty nodes)

Path Finding: DFS traversal with backtracking to find valid paths

File I/O: Read multiple tree configurations from input file, write results to output file

Error Handling: Comprehensive exception handling for robust execution

Time Complexity: O(N) where N is the number of nodes in the tree

⚡ Performance Characteristics<br>
Algorithm Efficiency:<br>
DFS Traversal: Visits each node exactly once

Backtracking: Efficient memory usage by reusing path list

Early Termination: No unnecessary computations beyond tree traversal

Memory Usage:<br>
Recursion Stack: Proportional to tree height O(H)

Path Storage: Only stores valid paths that match criteria

🛡️ Error Handling<br>
The implementation includes comprehensive error handling:

File Not Found: Graceful handling of missing input files

Invalid Input: Robust parsing of serialized tree data

Empty Trees: Proper handling of null/empty tree cases

Exception Propagation: Clear error messages for debugging

📊 Testing<br>
Test Cases Included:
Multiple valid paths in balanced tree

Single valid path scenarios

Negative numbers in paths

Trees with null nodes

Edge cases with root-only trees
