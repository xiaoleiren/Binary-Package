## Lab 2: Undefined Behavior in Binary
### 1. Setup

cd lab2-ub/
gcc -o ub_example source/ub_example.c

### 2. Predict

int overflow(int x) {
    return x * 2;
}

Question 1: What do you expect overflow(1500000000) to return? Why?

Question 2: Does the C standard guarantee this result? Explain.

### 3. Run & Trace
Use GDB to inspect the actual result:


gdb ./ub_example
(gdb) break overflow
(gdb) run
(gdb) print x
(gdb) print x*2

Question 3: What value does the binary actually compute?

Question 4: Why does the binary show this specific value?

### 4. Explain

1. Write a 150-word explanation covering:

2. What source-level semantics say about this operation

3. What the binary actually executed

4. Why the compiler made this choice

5. What this tells you about source-level vs binary-level reasoning

### 5. Reflection

How does this lab change your understanding of "undefined behavior"?


cat > labs/lab2-ub/source/ub_example.c 

#include <stdio.h>

int overflow(int x) {
return x * 2;
}

int main() {
int x = 1500000000;
int result = overflow(x);
printf("x = %d, x*2 = %d\n", x, result);
return 0;
}