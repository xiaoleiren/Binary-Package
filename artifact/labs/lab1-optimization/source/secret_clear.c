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