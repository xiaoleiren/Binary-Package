# Binary Gap Module: Source-to-Binary Reasoning for Security Education

## Overview

This repository contains the artifact package for the SIGCSE TS 2027 ERT paper:

> **"The Analyzer Said It Was Safe": Teaching Students to Verify Source-Level Guarantees at the Binary Level**

The module is a two-week binary security analysis unit designed to complement source-level program verification instruction. It consists of four scaffolded labs that progressively build students' ability to reason about the gap between source-level safety claims and binary-level execution.

## Quick Start

### Prerequisites

- Docker (20.10+) and Docker Compose
- 8 GB RAM minimum, 16 GB recommended
- 10 GB free disk space
- Modern browser for CTFd access

### One-Command Setup

```
git clone https://github.com/your-repo/binary-gap-module.git
cd binary-gap-module
docker-compose up -d
```

This launches:

CTFd at http://localhost:8000

A Ghidra server environment (accessible via X11 forwarding or VNC)

### Manual Setup

1. Install Ghidra 11.0.3, objdump, and GDB

2. Import CTFd challenges from ctf_config/export.zip

3. Use scripts/generate_seeds.py to create student-specific binaries

4. Distribute lab handouts from labs/*/handout.md

### Repository Structure
Path	Contents
labs/	Four lab handouts and solution notes
grading/	Rubrics and data collection templates
scripts/	Automation for binary generation and log extraction
data/	Sample anonymized CTF logs
docker/	Containerized environment definitions

### Lab Sequence
Lab	Topic	Core Concept
1	Compiler Optimization & Security	Dead-store elimination under -O2
2	Undefined Behavior in Binary	UB as concrete compiler manifestation
3	Rust/C FFI Boundaries	Unsafe contracts across languages
4	Integrated CTF Challenge	Synthesis across all patterns

### Grading Philosophy
Do not grade only the flag. Each lab requires:
Binary evidence (GDB trace or Ghidra screenshot)

Source-to-binary explanation

Mitigation proposal

We provide rubrics in grading/rubric.md that weight explanation and evidence as 70% of the total score.

### Data Collection
Use scripts/extract_logs.py to export CTFd logs into the template format in grading/. The templates are:

concept_probe_template.csv — Pre/post concept inventory

failure_modes_template.csv — Stuck-point coding

lab_summary_template.csv — Completion and effort metrics

reasoning_rubric_template.csv — Report scores

### Adapting the Module
The module can be used as:

A two-week unit (recommended)

Four standalone labs

A capstone for a security course

### Optional Modifications
Replace Rust/FFI with C/Python extension boundary

Use IDA Pro or Binary Ninja instead of Ghidra

Replace CTFd with any submission system supporting file uploads

### License
This material is released under a Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0). See LICENSE for details.



