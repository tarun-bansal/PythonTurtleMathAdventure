#!/usr/bin/env python3
"""
Test script for Session 1 code examples
"""

import turtle
import sys

def test_square():
    """Test the square drawing code from Session 1"""
    print("Testing square drawing...")
    t = turtle.Turtle()
    t.speed(0)  # Fastest speed for testing

    # Draw a square
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)

    print("✓ Square drawing test completed")
    t.clear()
    return True

def test_get_lost():
    """Test the 'Get Lost' challenge code"""
    print("Testing 'Get Lost' challenge...")
    t = turtle.Turtle()
    t.speed(0)

    t.forward(50)
    t.left(30)
    t.forward(75)
    t.right(45)
    t.backward(25)

    print("✓ 'Get Lost' challenge test completed")
    t.clear()
    return True

def test_triangle():
    """Test the triangle shape detective code"""
    print("Testing triangle shape detective...")
    t = turtle.Turtle()
    t.speed(0)

    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(120)
    t.forward(100)

    print("✓ Triangle test completed")
    t.clear()
    return True

def test_import():
    """Test basic import and print"""
    print("Testing basic import...")
    try:
        import turtle
        print("Python is working! 🎉")
        print("✓ Import test completed")
        return True
    except ImportError as e:
        print(f"✗ Import failed: {e}")
        return False

def main():
    """Run all tests"""
    print("=" * 60)
    print("Session 1 Technical Tests")
    print("=" * 60)

    results = []

    # Run tests
    results.append(("Import test", test_import()))
    results.append(("Square drawing", test_square()))
    results.append(("Get Lost challenge", test_get_lost()))
    results.append(("Triangle shape", test_triangle()))

    # Summary
    print("\n" + "=" * 60)
    print("Test Summary:")
    print("=" * 60)

    all_passed = True
    for test_name, passed in results:
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"{status}: {test_name}")
        if not passed:
            all_passed = False

    print("\n" + "=" * 60)
    if all_passed:
        print("All tests passed! ✅")
    else:
        print("Some tests failed. ❌")

    # Keep window open
    turtle.done()

    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())