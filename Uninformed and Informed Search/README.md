# Uninformed and Informed Search Algorithms

## Uninformed Search
Uninformed search algorithms, also known as blind search algorithms, do not have any additional information about states beyond the problem definition. These algorithms explore the search space without any guidance. Examples include:
- **Breadth-First Search**: Explores all possible paths level by level before moving deeper. It guarantees the shortest path if the cost is uniform.
- **Depth-First Search**: Explores as far as possible along each branch before backtracking.

### Application in Drone Delivery:
For drone delivery optimization, uninformed search can be used for terrain exploration, ensuring that all potential routes are considered even if they are not optimized initially.

## Informed Search
Informed search algorithms use heuristics to guide the search process. They evaluate nodes based on the estimated cost to reach the goal. Examples include:
- **A***: Uses a heuristic to compute the total estimated cost from the start node to the goal node.
- **Greedy Best-First Search**: Expands the node that appears to be closest to the goal without considering the cost from the start node.

### Application in Drone Delivery:
Informed search algorithms are crucial for optimizing routes by predicting the most efficient pathways, leading to faster delivery times and reduced energy consumption.