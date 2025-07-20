import os
import subprocess
import sys
import time

# The name of the virtual environment directory
VENV_DIR = ".venv"

def install_virtualenv():
    """Install virtualenv package if not available."""
    print("Installing virtualenv package...")
    try:
        result = subprocess.run([sys.executable, "-m", "pip", "install", "virtualenv"], 
                              capture_output=True, text=True, timeout=60)
        if result.returncode == 0:
            print("✓ virtualenv installed successfully")
            return True
        else:
            print(f"✗ Failed to install virtualenv: {result.stderr}")
            return False
    except Exception as e:
        print(f"✗ Error installing virtualenv: {e}")
        return False

def create_venv_with_virtualenv(venv_path):
    """Create virtual environment using virtualenv package."""
    print("Creating virtual environment with virtualenv...")
    try:
        result = subprocess.run([sys.executable, "-m", "virtualenv", VENV_DIR], 
                              capture_output=True, text=True, timeout=120)
        if result.returncode == 0:
            print("✓ Virtual environment created successfully with virtualenv!")
            return True
        else:
            print(f"✗ virtualenv failed: {result.stderr}")
            return False
    except subprocess.TimeoutExpired:
        print("✗ virtualenv creation timed out")
        return False
    except Exception as e:
        print(f"✗ Error with virtualenv: {e}")
        return False

def main():
    """
    Main function to set up and activate the virtual environment using virtualenv.
    """
    print("--- Virtual Environment Setup (Alternative Method) ---")
    print(f"Python executable: {sys.executable}")
    print(f"Current directory: {os.getcwd()}")
    print()

    venv_path = os.path.join(os.getcwd(), VENV_DIR)
    
    if os.path.isdir(venv_path):
        print(f"Virtual environment '{VENV_DIR}' already exists. Skipping creation.")
    else:
        print(f"Virtual environment '{VENV_DIR}' not found.")
        
        # First, try to import virtualenv
        try:
            import virtualenv
            print("✓ virtualenv package is available")
        except ImportError:
            print("✗ virtualenv package not found")
            if not install_virtualenv():
                print("Cannot proceed without virtualenv. Please install manually:")
                print("pip install virtualenv")
                input("Press Enter to exit.")
                return
        
        # Create virtual environment using virtualenv
        if not create_venv_with_virtualenv(venv_path):
            print("Virtual environment creation failed.")
            print("\nAlternative manual steps:")
            print("1. Open Command Prompt as Administrator")
            print("2. Run: pip install virtualenv")
            print("3. Run: virtualenv .venv")
            print("4. Run: .venv\\Scripts\\activate.bat")
            input("Press Enter to exit.")
            return

    # Find activation script
    possible_scripts = [
        os.path.join(venv_path, "Scripts", "activate.bat"),
        os.path.join(venv_path, "Scripts", "activate"),
    ]
    
    activate_script = None
    for script in possible_scripts:
        if os.path.isfile(script):
            activate_script = script
            break

    if not activate_script:
        print("✗ Activation script not found!")
        if os.path.isdir(venv_path):
            print(f"Directory contents: {os.listdir(venv_path)}")
            scripts_dir = os.path.join(venv_path, "Scripts")
            if os.path.isdir(scripts_dir):
                print(f"Scripts directory contents: {os.listdir(scripts_dir)}")
        input("Press Enter to exit.")
        return

    print(f"✓ Found activation script: {activate_script}")

    # Create launcher
    batch_content = f'''@echo off
title Python Virtual Environment (virtualenv)
echo.
echo ====================================
echo   Python Virtual Environment Ready
echo ====================================
echo.
echo Created with: virtualenv
echo Location: {venv_path}
echo Python: {sys.executable}
echo.
echo Commands:
echo   pip install package_name
echo   python your_script.py  
echo   deactivate
echo.
call "{activate_script}"
'''
    
    batch_file = os.path.join(venv_path, "launch.bat")
    try:
        with open(batch_file, 'w') as f:
            f.write(batch_content)
        
        print("Launching new Command Prompt in 3 seconds...")
        time.sleep(3)
        
        subprocess.Popen(['start', 'cmd', '/k', batch_file], shell=True)
        print("✓ New Command Prompt launched!")
        
    except Exception as e:
        print(f"✗ Error creating launcher: {e}")
        print(f"Manually activate with: {activate_script}")
        input("Press Enter to exit.")

if __name__ == "__main__":
    main()
