import os
import subprocess
import sys

# The name of the virtual environment directory
VENV_DIR = ".venv"

def main():
    """
    Main function to set up and activate the virtual environment.
    """
    print("--- Virtual Environment Setup for Windows ---")

    # --- Step 1: Check if the virtual environment directory exists ---
    venv_path = os.path.join(os.getcwd(), VENV_DIR)
    
    if not os.path.isdir(venv_path):
        print(f"Virtual environment '{VENV_DIR}' not found.")
        print("Creating a new virtual environment... (This may take a moment)")
        
        try:
            # Execute: python -m venv .venv
            # We use sys.executable to ensure we use the same python that is running the script.
            subprocess.run([sys.executable, "-m", "venv", VENV_DIR], check=True, shell=True)
            print("Virtual environment created successfully!")
        except subprocess.CalledProcessError as e:
            print(f"Error creating virtual environment: {e}")
            print("Please ensure Python is installed and accessible in your PATH.")
            input("Press Enter to exit.") # Pause to let user read the error
            return
        except FileNotFoundError:
            print("Error: 'python' command not found.")
            print("Please ensure Python is installed and its location is in the system's PATH environment variable.")
            input("Press Enter to exit.") # Pause to let user read the error
            return
    else:
        print(f"Virtual environment '{VENV_DIR}' already exists. Skipping creation.")

    # --- Step 2: Activate the virtual environment in a new CMD window ---
    # The activation script for Windows
    activate_script = os.path.join(venv_path, "Scripts", "activate.bat")

    if not os.path.isfile(activate_script):
        print(f"Error: Activation script not found at '{activate_script}'")
        input("Press Enter to exit.")
        return

    print("\nLaunching a new Command Prompt with the virtual environment activated...")
    print("This script window will now close.")

    # Use 'cmd /k' to run the activation script and keep the new window open.
    # 'start' runs it in a completely new, separate window.
    subprocess.Popen(f'start cmd /k "{activate_script}"', shell=True)

if __name__ == "__main__":
    main()