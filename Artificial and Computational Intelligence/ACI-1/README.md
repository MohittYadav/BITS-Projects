📌 Problem Statement

In the fast-growing field of logistics and transportation, delivery drones have become increasingly important. One of the main challenges is to design an intelligent route planning system that ensures:

Efficient and timely deliveries

Avoidance of obstacles and no-fly zones

Adaptability to dynamic urban environments

🎯 Objective

Develop a Python application using uninformed search algorithms to plan optimal drone delivery routes. The application should consider:

Distance minimization

Delivery priorities

Obstacles (tall buildings, restricted areas)

No-fly zones

Environment Representation:

🟩 Green → Roads and buildings

⬛ Black → Obstacles

🟥 Red → No-fly zones

🔵 Blue → Delivery points

🧩 Implemented Algorithms

The following uninformed search algorithms are applied:

Uniform Cost Search (UCS)

Depth First Search (DFS)

Each algorithm is tested to find the shortest or feasible path from a user-defined start point to one or multiple delivery destinations.
 <strong>⚙️ Features</strong>

Accepts user input for start and destination nodes.

Implements search algorithms for route planning.

Computes and prints time and space complexity.

Modular and well-documented Python code.

📊 Complexity Analysis

Each algorithm outputs:

Time Complexity → Number of nodes explored.

Space Complexity → Maximum frontier size during search.

🛠️ Tech Stack

Language: Python 3

Libraries:

collections / heapq (for priority queues & data structures)<br>

<strong>✨ Future Improvements</strong>

Extend to informed search (A*, Greedy Best-First Search).

Incorporate real-world GIS data for better simulations.

Add visualization of paths over a city grid.

