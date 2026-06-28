# Lab 2: Undefined Behavior in Binary

## Overview

Students analyze a program with undefined behavior (signed integer overflow)
and observe how the compiler chooses to implement it.

## Key Concepts

- Undefined behavior in C/C++
- Compiler's freedom under UB
- Source-level vs binary-level behavior
- Implementation-defined vs undefined

## Prerequisites

- Understanding of integer types
- Basic GDB usage

## Files

- `source/ub_example.c` — Program with signed overflow
- `binaries/ub_example` — Compiled binary

## Expected Deliverables

1. Prediction of source-level behavior
2. GDB trace showing actual binary behavior
3. Explanation of why UB manifests as observed
4. Distinction between "binary did X" and "language guarantees X"

