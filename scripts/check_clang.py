import subprocess # For running clang-format
import sys
import os

def run_clang_format(path):
    """Run clang-format on a given path and report formatting issues."""
    # TODO change to directly call clang-format as Python package
    # https://github.com/ssciwr/clang-format-wheel
    result = subprocess.run(['clang-format', '-i', '-style=file', path], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error in processing {path}: {result.stderr}")
    elif result.stdout:
        print(f"Formatting issues found in {path}:\n{result.stdout}")

def main(paths):
    """Recursively go though the src / examples folder and check clang."""
    for path in paths:
        if os.path.exists(path):
            run_clang_format(path)
        else:
            print(f"Path not found: {path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python check_clang.py <path1> <path2> ...")
        sys.exit(1)
    main(sys.argv[1:])
