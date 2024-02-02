import os
import re

def check_file_exists(file_path):
    try:
        if not os.path.exists(file_path):
            raise Exception(f"Error: {file_path} not found.")
    except Exception as e:
        print(e)

def check_string_in_file(file_path, string):
    with open(file_path, 'r') as file:
        contents = file.read()
        try:
            if string not in contents:
                raise Exception(f"Error: {string} not found in {file_path}")
        except Exception as e:
            print(e)

# Check for Main README.md
check_file_exists('README.md')

# Check for docs/README.md
check_file_exists('docs/README.md')

# Check for docs/assets folder and docs/api.md
check_file_exists('docs/assets')
check_file_exists('docs/api.md')

# Check String in Main README.md
check_string_in_file('README.md', '📖 For more information about this library please read the documentation [here](./docs/)')

# Check Headers in docs/README.md
check_string_in_file('docs/README.md', '# Features')
check_string_in_file('docs/README.md', '# Usage')
check_string_in_file('docs/README.md', '# API')
check_string_in_file('docs/README.md', '# License')