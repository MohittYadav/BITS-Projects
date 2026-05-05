This project implements a greedy algorithm to optimize photoshoot scheduling for a photography studio. The solution helps Gopal (the photographer) and his team minimize total completion time by determining the optimal sequence for staging and photographing products using parallel processing principles.<br>

Business Context:<br>
Gopal runs a product photography studio where:

His team handles product staging (setup)

Gopal handles photography

While Gopal photographs one product, his team can stage another

Goal: Minimize total completion time for all photoshoots

🧠 Algorithm Implementation<br>
Greedy Optimization Strategy<br>
The solution sorts products by staging time in ascending order to minimize team waiting time and maximize parallel processing.
Time Complexity Analysis
Time Complexity: O(N log N) - dominated by sorting operation

Space Complexity: O(N) - for storing product tuples and result sequence

Algorithm Justification:<br>
Staging-First Sorting: Products with shorter staging times are prioritized to start photography earlier

Parallel Processing: Overlaps team staging with Gopal's photography work

Minimal Idle Time: Reduces Gopal's waiting time between photoshoots.<br>

Output Components:<br>
Product Sequence: Optimized order showing execution sequence

Total Time: Complete duration from start to finish of all photoshoots

Idle Time: Gopal's waiting time before starting photography work

Advanced Features:<br>
Auto File Opening: Output file automatically opens after generation (Windows/macOS/Linux)

Comprehensive Error Handling: Handles file errors, format issues, and data validation

Console Debugging: Displays parsed values for verification

Cross-Platform Compatibility: Works on Windows, macOS, and Linux systems

⚡ Performance & Optimization<br>
Efficiency Analysis:<br>
Sorting Complexity: O(N log N) using Python's Timsort algorithm

Linear Processing: O(N) for sum calculations and sequence generation

Memory Efficient: Uses only essential data structures without external dependencies

Why This Approach Works:<br>
Early Photography Start: Shortest staging products begin photography sooner

Continuous Workflow: Team always has next product to stage while Gopal photographs

Resource Utilization: Maximizes parallel work between team and photographer

🛡️ Error Handling & Validation<br>
The implementation includes comprehensive error checking:

File Operations: Handles missing files, permission issues, and I/O errors

Data Validation: Verifies input format, data types, and value consistency

Platform Detection: Automatically adapts file opening commands for different OS

Graceful Degradation: Provides helpful error messages without crashing

📊 Testing Scenarios<br>
Test Cases Covered:<br>
Standard Case: Multiple products with varying times

Edge Cases: Single product, identical staging times, zero times

Large Inputs: Performance validation with 100+ products

Boundary Values: Minimum and maximum time constraints

🔄 Alternative Approaches<br>
Considered Alternatives:<br>
Photo-Time Sorting: Sort by photography time (less effective for parallel work)

Ratio-Based Sorting: Stage/Photo ratio (increased complexity without significant benefit)

Dynamic Programming: Optimal but O(N²) complexity for marginal gains

Chosen Approach Benefits:<br>
Simplicity: Easy to understand and implement

Efficiency: Near-optimal results with O(N log N) complexity

Practicality: Well-suited for real-world scheduling scenarios
