#!/usr/bin/env python
# LLM Generated

import subprocess
import sys

files = ['jadecomosedice.py', 'main.py', 'constants.py']
results = []

for file in files:
    try:
        result = subprocess.run(
            [sys.executable, '-m', 'py_compile', file],
            capture_output=True,
            text=True,
            timeout=20
        )
        if result.returncode == 0:
            results.append(f"✓ {file}: OK")
        else:
            results.append(f"✗ {file}: FAILED\n{result.stderr}")
    except Exception as e:
        results.append(f"✗ {file}: ERROR - {str(e)}")

for result in results:
    print(result)
