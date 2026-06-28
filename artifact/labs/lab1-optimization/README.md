# Lab 1: Compiler Optimization and Security

## Overview

Students analyze a program that appears to clear a secret buffer before
returning. They compile it at -O0 and -O2 and compare the binaries.

## Key Concepts

- Dead-store elimination
- Compiler optimization levels
- Source-to-binary mapping
- Security implications of optimization

## Learning Objectives

After completing this lab, students will be able to:

1. Locate a source-level operation in a binary's disassembly
2. Explain why an operation present in source may be absent in binary
3. Propose mitigations against optimization-induced security risks

## Prerequisites

- Basic C programming
- Familiarity with command-line compilation
- Ghidra installation

## Files

- `source/secret_clear.c` — Source program
- `binaries/secret_clear_O0` — Compiled with -O0
- `binaries/secret_clear_O2` — Compiled with -O2
- `binaries/secret_clear_O3` — Compiled with -O3 (optional extension)

## Expected Deliverables

1. Annotated Ghidra listing showing the clearing function at -O0
2. Explanation of where the clearing code went at -O2
3. Security consequence explanation
4. Mitigation proposal (e.g., volatile, explicit barrier, dedicated API)

## Common Pitfalls

- Confusing decompiler view with actual disassembly
- Assuming absent code means "no security risk"
- Proposing "turn off optimizations" as the only mitigation

## Hint System

| Level | Hint |
|-------|------|
| 1 | Compare the disassembly listings side-by-side |
| 2 | Focus on the function that calls memset |
| 3 | Dead-store elimination removes writes not later read |
| 4 | Use `__attribute__((optimize("O0")))` or volatile |