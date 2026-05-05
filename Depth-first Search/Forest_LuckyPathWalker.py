class TreeNode:
    # A tree node for a binary tree
    def __init__(this, x):
        this.val = x  # Value of the node
        this.left = None  # Reference to left child node
        this.right = None  # Reference to right child node

# Depth-first Search to find paths that sum up to a given Lucky number
def dfs_find_paths(root, current_sum, lucky_number, current_path, all_paths):
    # Base case: If the current node is None, return
    if root is None:
        return

    # Update the current sum and path with the current node's value
    current_sum += root.val
    current_path.append(root.val)

    # Print information about the current node being visited
    print(f"Visiting Node: {root.val}, Current Sum: {current_sum}, Path: {current_path}")

    # Verifying if the current node is a leaf node
    if root.left is None and root.right is None:
        # If the sum equals the lucky number, a valid path is found
        if current_sum == lucky_number:
            print("Current Sum ", current_sum)
            print("Lucky no.", lucky_number)
            all_paths.append(list(current_path))
            print(f"Found a path: {current_path}")
        else:
            # If the sum does not equal the lucky number, print a message
            print(f"Leaf without a lucky number: {current_path}")

    # Recursively call the function for the left and right child nodes
    dfs_find_paths(root.left, current_sum, lucky_number, current_path, all_paths)
    dfs_find_paths(root.right, current_sum, lucky_number, current_path, all_paths)

    # For Backtracking, remove the last element from the current path
    current_path.pop()


def find_lucky_number_paths(root, lucky_number):
    all_paths = []  # For all the paths that sum up to the lucky number
    try:
        dfs_find_paths(root, 0, lucky_number, [], all_paths)
    except Exception as e:
        # we can throw exception instead of print
        print(f"No path found for the given lucky number {e}")
    return all_paths


# Function to build the tree from the list of node values
def build_tree(nodes_list):
    if not nodes_list:
        return None
    # Root creation of the tree
    root = TreeNode(nodes_list[0])
    queue = [root]
    i = 1
    # Iteratively build the tree using a queue
    while queue and i < len(nodes_list):
        current = queue.pop(0)
        if nodes_list[i] is not None:
            current.left = TreeNode(nodes_list[i])
            queue.append(current.left)
        i += 1
        if i < len(nodes_list) and nodes_list[i] is not None:
            current.right = TreeNode(nodes_list[i])
            queue.append(current.right)
        i += 1
    return root

# Function to read input from a file
def process_input_file(file_path):
    trees = []
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        for line in lines:
            data = line.strip().split('::')
            nodes_list = [int(val) if val.lower() != 'null' else None for val in data[0].split(',')]
            lucky_number = int(data[1])
            trees.append((nodes_list, lucky_number))
    # Exception handling for fileNot Found
    except FileNotFoundError:
        print("Error: File not found at path {file_path}")
    except Exception as e:
        print(f"Error: {e}")
    # OR we can throw custom exception
    return trees

# Function to write output of a file as specified in Sample Output
def process_output_file(file_path, results):
    with open(file_path, 'w') as file:
        for paths in results:
            path_strings = [', '.join(map(str, path)) for path in paths]
            file.write(';'.join(path_strings) + '\n')

# Main block which reads the input, processes and then writes the result to an output file
if __name__ == "__main__":

    # If you have created your local environment for project then update to relative path
    input_file_path = "inputPS10.txt"
    # If you have created your local environment for project then update to relative path
    output_file_path = "outputPS10.txt"
    input_data = process_input_file(input_file_path)
    output_data = []

    for nodes_list, lucky_number in input_data:
        root = build_tree(nodes_list)
        paths = find_lucky_number_paths(root, lucky_number)
        output_data.append(paths)

    process_output_file(output_file_path, output_data)
