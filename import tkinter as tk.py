import tkinter as tk

from optimal_algo import optimal_page_replacement


# Function to open screens for each algorithm
def open_algorithm_screen(algorithm):
    # Destroy previous frame
    main_frame.destroy()
    
    # Create new frame for the algorithm screen
    algorithm_frame = tk.Frame(root)
    algorithm_frame.pack()

    # Implement logic to display specific content for each algorithm
    if algorithm == "Optimal Algorithm":
        # Display content for Algorithm 1
        algorithm_label = tk.Label(algorithm_frame, text="Enter numbers separated by spaces:")
        algorithm_label.pack()

        # Entry widget to take input from the user
        entry = tk.Entry(algorithm_frame)
        entry.pack(pady=5)

        # Label for number of frames
        num_frames_label = tk.Label(algorithm_frame, text="Enter number of frames:")
        num_frames_label.pack()

        # Entry widget for number of frames
        num_frames_entry = tk.Entry(algorithm_frame)
        num_frames_entry.pack(pady=5)

        error_label = tk.Label(algorithm_frame, text="", fg="red")  # Label to display error messages
        error_label.pack()

        # Label to display page hit
        page_hit_label = tk.Label(algorithm_frame, text="Page Hit: ")
        page_hit_label.pack()

        # Label to display page faults
        page_faults_label = tk.Label(algorithm_frame, text="Page Faults: ")
        page_faults_label.pack()

        # Function to split input into a list of integers and simulate the algorithm
        def split_input():
            input_text = entry.get()
            num_frames = num_frames_entry.get()
            if ' ' not in input_text:
                error_label.config(text="Values must be separated by spaces.")
                return
            try:
                numbers = [int(num) for num in input_text.split()]  # Convert each element to integer
                num_frames = int(num_frames)
                error_label.config(text="")  # Clear error message if no error
                # Call function to simulate algorithm
                page_hit, page_faults = optimal_page_replacement(numbers, num_frames)
                # Update labels with results
                page_hit_label.config(text="Page Hit: " + str(page_hit))
                page_faults_label.config(text="Page Faults: " + str(page_faults))
            except ValueError:
                error_label.config(text="Invalid input. Please enter integers only.")

        # Button to trigger splitting the input and simulating the algorithm
        split_button = tk.Button(algorithm_frame, text="Get result", command=split_input)
        split_button.pack(pady=5)

    elif algorithm == "Algorithm 2":
        # Display content for Algorithm 2
        algorithm_label = tk.Label(algorithm_frame, text="Algorithm 2 Screen")
        algorithm_label.pack()
    elif algorithm == "Algorithm 3":
        # Display content for Algorithm 3
        algorithm_label = tk.Label(algorithm_frame, text="Algorithm 3 Screen")
        algorithm_label.pack()
    elif algorithm == "Algorithm 4":
        # Display content for Algorithm 4
        algorithm_label = tk.Label(algorithm_frame, text="Algorithm 4 Screen")
        algorithm_label.pack()

# Function to create the main screen
def create_main_screen():
    global main_frame
    main_frame = tk.Frame(root)
    main_frame.pack()

    # Add buttons for each algorithm
    algorithms = ["Optimal Algorithm", "Algorithm 2", "Algorithm 3", "Algorithm 4"]
    for algorithm in algorithms:
        button = tk.Button(main_frame, text=algorithm, command=lambda alg=algorithm: open_algorithm_screen(alg))
        button.pack(pady=10)

# Main Tkinter window
root = tk.Tk()
root.title("Algorithm Selector")

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set window size to match screen width and height
root.geometry("%dx%d+0+0" % (screen_width, screen_height))

# Create main screen
create_main_screen()

# Run the Tkinter event loop
root.mainloop()
