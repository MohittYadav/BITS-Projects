import subprocess
import platform


# Function to read the input file provided
def read_input(input_file):
    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()
            # Find the line index where the actual data starts
            start_index = 0
            for index, line in enumerate(lines):
                if "Products:" in line:
                    start_index = index
                    break

            # Extract products, staging times, and photo times from the remaining lines
            products = lines[start_index].strip().split(":")[1].strip().split('/')
            staging_times = [int(time.strip()) for time in
                             lines[start_index + 1].strip().split(":")[1].strip().split('/')]
            photo_times = [int(time.strip()) for time in
                           lines[start_index + 2].strip().split(":")[1].strip().split('/')]

            # Prints the values read from the input file in console for check
            print("Products:", products)
            print("Staging Times:", staging_times)
            print("Photo Times:", photo_times)

        return products, staging_times, photo_times
    except FileNotFoundError:
        print("Input file not found:", input_file)
        return [], [], []
    except ValueError as e:
        print("Error converting time values to integers: Check for spaces", e)
        return [], [], []
    except Exception as e:
        print("An error occurred while reading input:", e)
        return [], [], []


# Function to write the output file
def write_output(output_text):
    try:
        with open("OutputPS10.txt", "w") as file:
            file.write(output_text)
            # Print a message in console indicating successful file writing
            print("Check popped-up OutputPS10.txt")
        # Pop up the output file
        pop_up_output_file("OutputPS10.txt")
    except Exception as e:
        print("An error occurred:", e)


# Function to pop_up the Output file
def pop_up_output_file(file_path):
    try:
        if platform.system() == 'Windows':  # Windows
            subprocess.Popen(['notepad.exe', file_path])
        elif platform.system() == 'Darwin':  # macOS
            subprocess.Popen(['open', file_path])
        elif platform.system() == 'Linux':  # Linux
            subprocess.Popen(['gedit', file_path])
        else:
            print("Unable to pop up output file. Unsupported operating system. Check console for the same")
    except Exception as e:
        print("An error occurred while popping up output file:", e)


def greedy_optimization_photoshoot(products, staging_times, photo_times):
    # Combine product data into a list of tuples (product, staging_time, photo_time)
    product_data = list(zip(products, staging_times, photo_times))

    # Sort products in ascending order according to staging_times
    sorted_products = sorted(product_data, key=lambda x: x[1])

    # Initialization of variables
    product_sequence = []
    total_time = 0
    idle_time = 0
    total_photo_time = 0

    # Iterate through sorted products and calculate total time and idle time
    for product in sorted_products:
        product_name, staging_time, photo_time = product
        idle_time = sorted_products[0][1]
        total_photo_time += photo_time
        product_sequence.append(product[0])
    total_time += total_photo_time + idle_time

    return product_sequence, total_time, idle_time

# Main block which reads the input, calls the function and then writes the result to an output file
def main():
    input_file = "C:/Users/mohit/OneDrive/Desktop/inputPS10.txt"  # Please provide the path here of the input file

    # Read input
    products, staging_times, photo_times = read_input(input_file)

    # Optimize photoshoot
    product_sequence, total_time, idle_time = greedy_optimization_photoshoot(products, staging_times, photo_times)

    # Prepare output text
    output_text = "Product Sequence: " + ", ".join(product_sequence) + "\n"
    output_text += "Total time to complete photoshoot: " + str(total_time) + " minutes\n"
    output_text += "Idle time for Gopal: " + str(idle_time) + " minutes\n"

    # Write output to file and pop it up
    write_output(output_text)
    print("Output check for console: ")
    print(output_text)


if __name__ == "__main__":
    main()
