#!/usr/bin/env python
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

for result in results:
    print(result)
