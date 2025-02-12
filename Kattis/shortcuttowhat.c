// https://open.kattis.com/problems/shortcuttowhat

#include <stdio.h>
#include <stdlib.h>

int solve(int n) {
    return (n +5) * 3 - 10;
}

int main() {
    // Allocate memory for n:
    int *n = (int *)calloc(1, sizeof(int));
    if (n == NULL) {
        fprintf(stderr, "Error allocating memory for n.");
        return 1;
    }

    // Read input:
    char buffer[5];
    fgets(buffer, sizeof(buffer), stdin);
    *n = atoi(buffer);
    
    // Give output:
    printf("%d\n", solve(*n));

    // Free allocated memory:
    free(n);
    
    return 0;
}