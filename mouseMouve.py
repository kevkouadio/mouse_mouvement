import tkinter as tk
import subprocess
import sys
import os

process = None

def run_script():
    global process

    script_path = os.path.join(os.path.dirname(__file__), "mouse_movement.py")
    python_executable = sys.executable

    # Start the script as a separate process
    process = subprocess.Popen([python_executable, script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Hide the "Run Script" button
    run_button.grid_remove()

    # Show the "Stop Script" button
    stop_button.grid(row=1, column=0, pady=50)

def stop_script():
    global process

    if process:
        # Terminate the running script
        process.terminate()
        process.wait()
        process = None

    # Hide the "Stop Script" button
    stop_button.grid_remove()

    # Show the "Run Script" button
    run_button.grid(row=1, column=0, pady=50)

# Create the main window
window = tk.Tk()
window.title("KevKouadio Mouse Movement")

# Set the window size to a default terminal size (80x24)
window.geometry("300x200")

# Create a label
label = tk.Label(window)
label.pack(fill=tk.BOTH, expand=True)

# Create a frame to hold the buttons
button_frame = tk.Frame(label)
button_frame.pack()

# Create a button to run the script
run_button = tk.Button(button_frame, text="Start", command=run_script, width=20, height=3)
run_button.grid(row=1, column=0, pady=50)

# Create a button to stop the script
stop_button = tk.Button(button_frame, text="Stop", command=stop_script, width=20, height=3)

# Start with the "Stop Script" button hidden
stop_button.grid_remove()

# Start the main event loop
window.mainloop()
