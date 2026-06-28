#!/usr/bin/env python3
"""
Generate seeded binaries for Lab 4.

Usage:
    python3 generate_seeds.py --students 50 --seed 42 --output ./binaries/
"""

import argparse
import os
import random
import subprocess
import sys
from pathlib import Path

def parse_args():
    parser = argparse.ArgumentParser(description="Generate seeded binaries")
    parser.add_argument("--students", type=int, default=50, help="Number of students")
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
    parser.add_argument("--output", default="./binaries/", help="Output directory")
    parser.add_argument("--source", default="./source/challenge.c", help="Source file")
    return parser.parse_args()

def generate_binary(student_id, seed, source_path, output_dir):
    """Generate a unique binary for each student."""
    output_dir.mkdir(parents=True, exist_ok=True)

    # Use seed to set constants, offsets, and optimization variants
    rng = random.Random(seed + student_id)

    # Randomize: flag offset (0-255), optimization flag, constants
    flag_offset = rng.randint(0, 255)
    opt_level = rng.choice(["-O0", "-O1", "-O2", "-Os"])

    # Write a header file with student-specific constants
    header_path = output_dir / f"config_s{student_id}.h"
    with open(header_path, "w") as f:
        f.write(f"#define STUDENT_ID {student_id}\n")
        f.write(f"#define FLAG_OFFSET {flag_offset}\n")
        f.write(f"#define SEED_CONSTANT {rng.randint(1, 1000000)}\n")

    # Compile
    binary_path = output_dir / f"challenge_s{student_id}"
    cmd = [
        "gcc",
        source_path,
        f"-I{output_dir}",
        opt_level,
        "-o", str(binary_path),
        "-D", f"STUDENT_ID={student_id}",
        "-D", f"FLAG_OFFSET={flag_offset}"
    ]

    subprocess.run(cmd, check=True)

    # Record metadata for autograder
    with open(output_dir / "metadata.csv", "a") as f:
        f.write(f"{student_id},{binary_path},{flag_offset},{opt_level},{seed}\n")

    return binary_path, flag_offset, opt_level

def main():
    args = parse_args()
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Clear metadata file
    with open(output_dir / "metadata.csv", "w") as f:
        f.write("student_id,binary_path,flag_offset,optimization,seed\n")

    for i in range(1, args.students + 1):
        generate_binary(i, args.seed + i, args.source, output_dir)

    print(f"Generated {args.students} seeded binaries in {output_dir}")

if __name__ == "__main__":
    main()