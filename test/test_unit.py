import os
import subprocess


def execute_test_files(directory_path):
    if not os.path.exists(directory_path):
        print(f"Directory '{directory_path}' does not exist.")
        return

    test_files = [filename for filename in os.listdir(directory_path) if filename.endswith('.py')]

    if not test_files:
        print(f"No test files found in '{directory_path}'.")
        return

    for test_file in test_files:
        test_file_path = os.path.join(directory_path, test_file)
        print(f"Executing '{test_file}'...")
        try:
            subprocess.run(['python', test_file_path], check=True)
            print(f"'{test_file}' executed successfully.\n")
        except subprocess.CalledProcessError:
            print(f"Error executing '{test_file}'.\n")


if __name__ == "__main__":
    test_directory = "test_units"  # Replace with the actual directory path
    execute_test_files(test_directory)
