import subprocess
import os
import sys

# state error
result = subprocess.run(['clang-format','--dry-run', '--Werror', './sketches/blink/blink.ino'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output = result.stdout.decode() + result.stderr.decode() 

print(output)

# Identify number of errors, based on the output
error_count = output.count('error:')

print(f"Number of errors: {error_count}")
