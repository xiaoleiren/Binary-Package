# Lab 1: Compiler Optimization and Security

## 1. Setup

```
cd lab1-optimization/
gcc -O0 -o secret_clear_O0 source/secret_clear.c
gcc -O2 -o secret_clear_O2 source/secret_clear.c
```
## 2. Source Code Analysis
Review source/secret_clear.c:

#include <string.h>
#include <stdlib.h>
#include <stdio.h>

void clear_secret(char *buf, size_t len) {
    memset(buf, 0, len);
}

int main() {
    char secret[32] = "SuperSecretPassword123!";
    printf("Secret: %s\n", secret);
    clear_secret(secret, 32);
    printf("Secret after clear: %s\n", secret);
    return 0;
}

Question 1: Where is the security-critical operation?

Question 2: What guarantees does this provide at source level?

## 3. Binary Inspection
Open both binaries in Ghidra. Navigate to the clear_secret function.

Question 3: What do you observe at -O0?

Question 4: What do you observe at -O2?

Question 5: If present, what is the security risk? If absent, why?

## 4. Explanation

1. Write a 200-word explanation covering:

2. What source-level analysis would conclude about this code

3. What the binary actually does

4. Why the compiler made this transformation

The security implication

## 5. Mitigation
Propose at least two ways to ensure the secret is actually cleared:

One using a compiler attribute

One using a language-level approach

## 6. Reflection
What surprised you most about this lab? How does it change your view of
source-level guarantees?



