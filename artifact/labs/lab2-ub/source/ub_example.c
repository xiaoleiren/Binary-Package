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