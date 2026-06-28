# Lab 4: Integrated CTF Challenge

## 1. Overview
This lab combines all three patterns from Labs 1-3 into a single binary.
Your task is to:

- Find the flag
- Explain the source-to-binary reasoning for each pattern
- Provide evidence (GDB trace, Ghidra annotations)
- Propose mitigations

## 2. Binary
You have received a seeded binary with unique constants and layout.

./challenge_s<student_id>

## 3. Required Evidence
GDB trace: Breakpoints showing each key pattern
Ghidra annotations: Screenshots or annotated project file
Reasoning report: Explanation of each pattern

## 4. Grading Weight
Flag (30%)
Source-to-binary explanation (40%)
Mitigation + evidence (30%)

## 5. Submission
Submit the following files:

- flag.txt — The captured flag
- gdb_trace.txt — GDB command history and output
- ghidra_annotations.png or .txt — Analysis evidence
- report.pdf or .md — Source-to-binary reasoning report

## 6. Hints
Level	Hint
1	Each earlier lab pattern appears in a different function
2	Check optimization levels and UB in the binary
3	The flag is derived from a runtime value
4	Follow the execution flow with GDB

cat > labs/lab4-ctf/source/challenge.c 

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// Pattern 1: Dead-store elimination (Lab 1)
void clear_secret(char *buf, size_t len) {
memset(buf, 0, len); // May be optimized away
}

// Pattern 2: Undefined behavior (Lab 2)
int ub_operation(int x) {
return x * 2; // Signed overflow if x > INT_MAX/2
}

// Pattern 3: FFI boundary (Lab 3)
extern void c_process(unsigned char *buf, size_t len);

int main() {
char secret[32] = "CTF{...}";
int x = 1500000000;
unsigned char data[5] = {1, 2, 3, 4, 5};

// Apply all patterns
clear_secret(secret, 32);
int result = ub_operation(x);
c_process(data, 5);

printf("Result: %d\n", result);
return 0;
}

