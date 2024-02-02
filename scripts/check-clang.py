import subprocess
import os
import sys

# Function to run clang-format on a file
def run_clang_format(file_path):
    result = subprocess.run(['clang-format', '--dry-run', '--Werror', file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = result.stdout.decode() + result.stderr.decode()
    return output

# Function to recursively run clang-format on a folder and its subfolders
def run_clang_format_on_folder(folder_path):
    error_count = 0
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.ino'):
                file_path = os.path.join(root, file)
                output = run_clang_format(file_path)
                print(output)
                error_count += output.count('error:')
    print(f"Number of errors: {error_count}")

# Run clang-format on the specified folder
print("Starting clang-format on src folders")
run_clang_format_on_folder('./src')
print("Finished clang-format on src folders")

print("Starting clang-format on examples folders")
run_clang_format_on_folder('./examples')
print("Finished clang-format on examples folders")

