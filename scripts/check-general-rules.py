import os
import re
import subprocess

def read_library_properties():
    try:
        with open('library.properties', 'r') as file:
            return file.read()
    except Exception as e:
        print(e)

def determine_cpp_version(library_properties):
    if "architectures=\\*" in library_properties:
        return "C++11"
    elif "renesas_portenta" in library_properties:
        return "C++17"
    elif "mbed_opta" in library_properties:
        return "C++14"
    elif "mbed_portenta" in library_properties:
        return "C++14"
    else:
        return "Unknown"

def check_line_length():
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith('.cpp') or file.endswith('.h') or file.endswith('.ino'):
                file_path = os.path.join(root, file)
                result = subprocess.run(['clang-format', '-style={ColumnLimit: 120}', file_path], capture_output=True, text=True)
                try:
                    if result.stdout != open(file_path).read():
                        raise Exception(f"Error: File {file_path} does not meet the line length requirement.")
                except Exception as e:
                    print(e)

def check_cast_comments():
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith('.cpp') or file.endswith('.h') or file.endswith('.ino'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    content = f.read()
                    try:
                        if re.search(r"(static_cast<.*?>|reinterpret_cast<.*?>|\(.*?\)).*(?<!//.*)", content):
                            raise Exception(f"Error: Found a cast without a comment in {file_path}")
                    except Exception as e:
                        print(e)

def main():
    library_properties = read_library_properties()
    cpp_version = determine_cpp_version(library_properties)
    print(f"C++ Version is {cpp_version}")
    check_line_length()
    check_cast_comments()

if __name__ == "__main__":
    main()