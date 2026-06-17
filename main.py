# main.py
import subprocess
import sys
from record_time import timer
def run_script(script_name):
    """
    Executes a specific Python file and waits for it to finish.
    """
    print(f"--- Starting: {script_name} ---")
    
    # sys.executable automatically finds the path of your current Python interpreter.
    # subprocess.run runs the script as if you typed 'python script_name.py' in the terminal.
    result = subprocess.run([sys.executable, script_name])
    
    # A return code of 0 means the script finished successfully without any crashes.
    if result.returncode == 0:
        print(f"--- Finished: {script_name} successfully ---\n")
        return True
    else:
        print(f"❌ Error: {script_name} failed! Stopping the workflow.")
        return False

@timer
def main():
    # Step 1: Run the first file.
    # Replace "file1.py" with your actual file name.
    if run_script("scraper.py"):
        # Step 2: Run the second file ONLY if the first one finishes successfully.
        # Replace "file2.py" with your actual file name.
        run_script("visualize.py")

# This ensures main() only runs if you execute this specific file directly.
if __name__ == "__main__":
    main()
