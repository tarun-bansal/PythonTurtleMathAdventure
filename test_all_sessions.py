#!/usr/bin/env python3
"""
Comprehensive test of code examples from all sessions
Tests syntax and basic logic without GUI dependencies
"""

import ast
import sys
import os
import keyword
from pathlib import Path

def extract_python_code_from_md(md_file):
    """Extract Python code blocks from markdown file"""
    with open(md_file, 'r') as f:
        content = f.read()

    code_blocks = []
    lines = content.split('\n')
    in_code_block = False
    current_block = []

    for line in lines:
        if line.strip().startswith('```python'):
            in_code_block = True
            current_block = []
        elif line.strip().startswith('```') and in_code_block:
            in_code_block = False
            if current_block:
                code_blocks.append('\n'.join(current_block))
        elif in_code_block:
            current_block.append(line)

    return code_blocks

def test_code_syntax(code, block_num):
    """Test if Python code has valid syntax"""
    try:
        ast.parse(code)
        return True, None
    except SyntaxError as e:
        return False, f"Syntax error in block {block_num}: {e}"
    except Exception as e:
        return False, f"Error in block {block_num}: {e}"

def test_session(session_file):
    """Test all code blocks in a session file"""
    print(f"\n{'='*60}")
    print(f"Testing: {session_file}")
    print('='*60)

    if not os.path.exists(session_file):
        print(f"File not found: {session_file}")
        return []

    code_blocks = extract_python_code_from_md(session_file)
    results = []

    for i, code in enumerate(code_blocks, 1):
        if not code.strip():
            continue

        # Skip very short code blocks (likely incomplete examples)
        if len(code.strip().split('\n')) < 2:
            continue

        # Check for common issues
        issues = []

        # Check syntax
        valid, error = test_code_syntax(code, i)
        if not valid:
            issues.append(error)
            results.append((i, False, issues))
            continue

        # Check for common beginner issues
        lines = code.split('\n')

        # Check for missing imports in standalone examples
        has_turtle_commands = any('turtle.' in line or 'import turtle' in line for line in lines)
        has_import = any('import turtle' in line for line in lines)

        if has_turtle_commands and not has_import:
            issues.append("Missing 'import turtle' for turtle commands")

        # Check for undefined variables in simple examples
        # (This is a basic check - not comprehensive)
        defined_vars = set()
        for line_num, line in enumerate(lines, 1):
            # Simple check for variable assignments
            if '=' in line and not line.strip().startswith('#'):
                parts = line.split('=')
                if len(parts) > 0:
                    var_name = parts[0].strip()
                    if var_name and not var_name.startswith(('print', 'if', 'for', 'while', 'def')):
                        defined_vars.add(var_name)

            # Check for variable usage
            for word in line.replace('.', ' ').replace('(', ' ').replace(')', ' ').split():
                if word in ['t', 'screen', 'turtle']:
                    continue  # Common turtle objects
                if word.isidentifier() and not keyword.iskeyword(word):
                    # Check if it's used before being defined (in this simple example)
                    # This is not perfect but catches obvious issues
                    if '=' not in line and word not in defined_vars and not any(
                        kw in line for kw in ['import', 'def', 'class', 'for', 'in']
                    ):
                        # Skip common built-ins and functions
                        if word not in ['print', 'input', 'int', 'str', 'range', 'len', 'abs']:
                            issues.append(f"Line {line_num}: Variable '{word}' might be used before definition")

        results.append((i, True, issues))

    return results

def main():
    """Test all session files"""
    base_dir = Path("/home/tarun-bansal/PythonTurtleMathAdventure/sessions")

    if not base_dir.exists():
        print(f"Directory not found: {base_dir}")
        return 1

    all_results = {}
    session_files = sorted(base_dir.glob("session*/session*.md"))

    print("Python Turtle Math Adventure - Technical Code Review")
    print("="*60)

    for session_file in session_files:
        session_name = session_file.parent.name
        results = test_session(session_file)
        all_results[session_name] = results

        # Print summary for this session
        total_blocks = len(results)
        passed_blocks = sum(1 for _, passed, _ in results if passed)
        failed_blocks = total_blocks - passed_blocks

        print(f"\n{session_name}:")
        print(f"  Code blocks: {total_blocks}")
        print(f"  Passed: {passed_blocks}")
        print(f"  Failed: {failed_blocks}")

        # Print details for failed blocks
        for block_num, passed, issues in results:
            if not passed or issues:
                print(f"  Block {block_num}: {'PASS' if passed else 'FAIL'}")
                for issue in issues:
                    print(f"    - {issue}")

    # Overall summary
    print("\n" + "="*60)
    print("OVERALL SUMMARY")
    print("="*60)

    total_blocks_all = sum(len(results) for results in all_results.values())
    total_passed_all = sum(
        sum(1 for _, passed, _ in results if passed)
        for results in all_results.values()
    )
    total_failed_all = total_blocks_all - total_passed_all

    print(f"Total code blocks tested: {total_blocks_all}")
    print(f"Total passed: {total_passed_all}")
    print(f"Total failed: {total_failed_all}")

    if total_failed_all == 0:
        print("\n✅ All code blocks have valid syntax!")
    else:
        print(f"\n❌ {total_failed_all} code blocks have issues")

    return 0 if total_failed_all == 0 else 1

if __name__ == "__main__":
    sys.exit(main())