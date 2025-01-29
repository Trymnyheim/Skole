// https://open.kattis.com/submissions/15313842

#include <stdio.h>
#include <stdlib.h>

int main() {
    // Buffer for reading input:
    char buffer[20];

    // Allocate and read value of n:
    int *n = (int *)malloc(sizeof(int));
    if (n == NULL) {
        fprintf(stderr, "Failed to allocate memory for n.");
        return 1;
    }
    fgets(buffer, sizeof(buffer), stdin);
    *n = atoi(buffer);

    // Allocate and read ages:
    int *ages = (int *)malloc(*n * sizeof(int));
    if (ages == NULL) {
        fprintf(stderr, "Failed to allocate memory for ages.");
        return 1;
    }
    for (int i = 0; i < *n; i++) {
        fgets(buffer, sizeof(buffer), stdin);
        ages[i] = atoi(buffer);
    }

    // Find min age:
    int min = ages[0];
    for (int i = 1; i < *n; i++) {
        if (ages[i] < min) {
            min = ages[i];
        }
    }
    // Output:
    printf("%d", min);
    return 0;
}