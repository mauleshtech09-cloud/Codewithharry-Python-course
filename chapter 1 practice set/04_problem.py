# Import the os module
# The os module allows Python to interact with the operating system
import os


# Define the directory path
# "." means the current working directory where this script is located
path = "/USEC"


# Use os.listdir() to get a list of all files and folders in the directory
contents = os.listdir(path)


# Loop through each item returned by os.listdir()
for item in contents:

    # Create the full path of the item
    # os.path.join() safely combines directory path and file name
    full_path = os.path.join(path, item)

    # Check if the item is a directory
    if os.path.isdir(full_path):
        print("Directory:", item)

    # If it is not a directory, it must be a file
    else:
        print("File:", item)