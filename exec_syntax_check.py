# LLM Generated

import py_compile
import sys

files = ['jadecomosedice.py', 'main.py', 'constants.py']
results = []

for file in files:
    try:
        py_compile.compile(file, doraise=True)
        results.append(f"✓ {file}: OK")
    except py_compile.PyCompileError as e:
        results.append(f"✗ {file}: FAILED\n{str(e)}")
    except Exception as e:
        results.append(f"✗ {file}: ERROR - {str(e)}")

output = '\n'.join(results)
print(output)

with open('syntax_check_output.txt', 'w') as f:
    f.write(output)
