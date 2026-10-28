#!/usr/bin/env python

# LLM generated

"""Temporary runner to execute syntax_check.py and capture output."""
import subprocess
import sys
import os

os.chdir(r'c:\Users\jaded\Documents\Workspace\Python3\JadeComoSeDice')
result = subprocess.run([sys.executable, 'syntax_check.py'], capture_output=True, text=True)
print(result.stdout)
if result.stderr:
    print("STDERR:", result.stderr, file=sys.stderr)
sys.exit(result.returncode)
