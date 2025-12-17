#!/usr/bin/env python3
"""
Debug specific issues found in the code review
"""

import ast
import re

def examine_file(filepath):
    """Examine a session file for issues"""
    print(f"\nExamining: {filepath}")
    print("="*60)

    with open(filepath, 'r') as f:
        content = f.read()

    # Find all code blocks
    pattern = r'```python\n(.*?)```'
    blocks = re.findall(pattern, content, re.DOTALL)

    for i, block in enumerate(blocks, 1):
        block = block.strip()
        if not block:
            continue

        print(f"\n--- Block {i} ---")
        # Show first few lines
        lines = block.split('\n')
        preview = '\n'.join(lines[:5])
        if len(lines) > 5:
            preview += "\n..."
        print(preview)

        # Check syntax
        try:
            ast.parse(block)
            print("✓ Syntax OK")
        except SyntaxError as e:
            print(f"✗ Syntax error: {e}")
            print("Full block:")
            print(block)

        # Check for indentation issues
        lines = block.split('\n')
        for line_num, line in enumerate(lines, 1):
            if line.strip() and not line.startswith(' ') and line_num > 1:
                # Check if this line should be indented (follows a colon)
                if line_num > 1 and lines[line_num-2].strip().endswith(':'):
                    print(f"  Warning line {line_num}: Possible missing indentation after ':'")
                    print(f"    Previous line: {lines[line_num-2]}")
                    print(f"    Current line: {line}")

# Check session02
examine_file("sessions/session02/session02.md")

# Check other sessions with issues
examine_file("sessions/session05/session05.md")
examine_file("sessions/session07/session07.md")