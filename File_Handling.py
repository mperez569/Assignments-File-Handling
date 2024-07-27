#1. Exploring Python's OS Module
#Task 1: Directory Inspector:
Assignments: File Handling
import os

def directory_contents(path):
    try:
        # List all files and subdirectories in the given path
        with os.scandir(path) as entries:
            print(f"Contents of '{path}':")
          
            for entry in entries:
                if entry.is_file():
                    print(f"File: {entry.name}")
                  
                elif entry.is_dir():
                    print(f"Directory: {entry.name}")
                  
    except FileNotFoundError:
        print("Error: The specified directory does not exist.")
      
    except PermissionError:
        print("Error: You do not have permission to access this directory.")
      
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    path = input("Enter the directory path: ")
    directory_contents(path)

main()
