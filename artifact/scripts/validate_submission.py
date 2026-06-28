#!/usr/bin/env python3
"""
Validate student submission: check binary hash, GDB trace, and required files.

Usage:
    python3 validate_submission.py --student S001 --submission ./submissions/S001/
"""

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

def parse_args():
    parser = argparse.ArgumentParser(description="Validate submission")
    parser.add_argument("--student", required=True, help="Student ID")
    parser.add_argument("--submission", required=True, help="Submission directory")
    parser.add_argument("--metadata", default="./binaries/metadata.csv", help="Metadata file")
    return parser.parse_args()

def check_binary_hash(submission_dir, expected_hash, student_id):
    """Verify the submitted binary hash matches the expected value."""
    binary_path = submission_dir / f"challenge_s{student_id}"
    if not binary_path.exists():
        return False, "Binary file missing"

    actual_hash = hashlib.sha256(open(binary_path, "rb").read()).hexdigest()
    if actual_hash != expected_hash:
        return False, f"Hash mismatch: expected {expected_hash[:8]}..., got {actual_hash[:8]}..."

    return True, "Binary hash verified"

def check_gdb_trace(submission_dir):
    """Check that GDB trace contains required evidence."""
    trace_path = submission_dir / "gdb_trace.txt"
    if not trace_path.exists():
        return False, "GDB trace missing"

    content = trace_path.read_text()

    # Look for evidence of breakpoint and memory dump
    if "break" not in content.lower() and "b " not in content.lower():
        return False, "No breakpoint found in GDB trace"

    if "x/" not in content and "print" not in content.lower():
        return False, "No memory inspection found in GDB trace"

    return True, "GDB trace validated"

def check_ghidra_annotations(submission_dir):
    """Check that Ghidra annotations are present."""
    annotation_path = submission_dir / "ghidra_annotations.txt"
    if not annotation_path.exists():
        # Try alternative: screenshot
        screenshot_path = submission_dir / "ghidra_screenshot.png"
        if not screenshot_path.exists():
            return False, "No Ghidra annotations or screenshot found"
        return True, "Ghidra screenshot present"

    content = annotation_path.read_text()
    # Check for evidence of actual analysis
    if len(content.strip()) < 100:
        return False, "Ghidra annotations too brief"

    return True, "Ghidra annotations validated"

def main():
    args = parse_args()
    submission_dir = Path(args.submission)

    if not submission_dir.exists():
        print(f"ERROR: Submission directory {submission_dir} not found")
        sys.exit(1)

    # Load metadata
    metadata_path = Path(args.metadata)
    if not metadata_path.exists():
        print("WARNING: Metadata file not found; skipping binary hash check")
        expected_hash = None
    else:
        # In practice, look up expected hash by student ID
        expected_hash = "dummy_hash_32chars"

    results = {}

    # Check binary
    if expected_hash:
        ok, msg = check_binary_hash(submission_dir, expected_hash, args.student)
        results["binary"] = {"passed": ok, "message": msg}
    else:
        results["binary"] = {"passed": True, "message": "Skipped (no metadata)"}

    # Check GDB trace
    ok, msg = check_gdb_trace(submission_dir)
    results["gdb_trace"] = {"passed": ok, "message": msg}

    # Check Ghidra annotations
    ok, msg = check_ghidra_annotations(submission_dir)
    results["ghidra"] = {"passed": ok, "message": msg}

    # Overall result
    all_passed = all(v["passed"] for v in results.values())

    print(json.dumps(results, indent=2))
    print(f"\nOverall: {'PASSED' if all_passed else 'FAILED'}")

    sys.exit(0 if all_passed else 1)