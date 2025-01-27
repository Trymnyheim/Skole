// https://open.kattis.com/problems/sauna

#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

int main() {
    int n;
    scanf("%d", &n);
    // Allocate memory for temperatures:
    int *temps = (int *)malloc((n * 2) * sizeof(int));
    if (temps == NULL) {
        fprintf(stderr, "Failed to allocate memory.\n");
        return 1;
    }
    // Read temperatures:
    for (int i = 0; i < n * 2; i++) {
        scanf("%d", &temps[i]);
    }

    // Find min and max temperature:
    int min = 0;
    int max = INT_MAX;
    for (int i = 0; i < 2 * n; i+=2) {
        if (temps[i] > min) {
            min = temps[i];
        }
        if (temps[i+1] < max) {
            max = temps[i+1];
        }
    }

    // Give output:
    if (min <= max) {        
        printf("%d %d", max - min + 1, min);
    }
    else {
        printf("bad news");
    }

    // Free allocated memory
    free(temps);

    return 0;
}