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