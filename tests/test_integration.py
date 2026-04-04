#!/usr/bin/env python3
"""Integration test for the C++ engine binary."""

import subprocess
import os
import sys


def test_engine_execution():
    """Test that the engine binary executes successfully."""
    
    # Find the binary - Bazel places data dependencies in specific locations
    # When run via bazel test, the binary will be in the runfiles
    binary_path = "core/engine_main"
    
    # Check if we're running under Bazel
    if "TEST_SRCDIR" in os.environ and "TEST_WORKSPACE" in os.environ:
        workspace = os.environ["TEST_WORKSPACE"]
        srcdir = os.environ["TEST_SRCDIR"]
        binary_path = os.path.join(srcdir, workspace, binary_path)
    
    print(f"Testing binary: {binary_path}")
    
    # Run the binary
    try:
        result = subprocess.run(
            [binary_path],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        print(f"STDOUT:\n{result.stdout}")
        print(f"STDERR:\n{result.stderr}")
        print(f"Return code: {result.returncode}")
        
        # Assert that the binary executed successfully
        assert result.returncode == 0, (
            f"Engine binary failed with return code {result.returncode}. "
            f"Stderr: {result.stderr}"
        )
        
        print("✓ Engine binary executed successfully")
        
    except subprocess.TimeoutExpired:
        raise AssertionError("Engine binary timed out after 10 seconds")
    except FileNotFoundError:
        raise AssertionError(f"Binary not found at {binary_path}")


if __name__ == "__main__":
    try:
        test_engine_execution()
        print("\n✓ All tests passed!")
        sys.exit(0)
    except AssertionError as e:
        print(f"\n✗ Test failed: {e}", file=sys.stderr)
        sys.exit(1)
