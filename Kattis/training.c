// https://open.kattis.com/problems/training

#include <stdio.h>
#include <stdlib.h>

int main() {
    // Allocate memory and read input:
    int n, level;
    scanf("%d %d", &n, &level);
    int **pairs = (int **)malloc(n * sizeof(int *));
    if (pairs == NULL) {
        fprintf(stderr, "Failed to allocate memory for array.");
        return 1;
    }

    for (int i = 0; i < n; i++) {
        pairs[i] = (int *)malloc(2 * sizeof(int));
        if (pairs[i] == NULL) {
            fprintf(stderr, "Failed to allocate memory for pair nr. %d.", i);
            for (int j = 0; j < i; j++) {
                free(pairs[j]);
            }
            free(pairs);
            return 1;
        }
        scanf("%d %d", &pairs[i][0], &pairs[i][1]);
    }

    // Perform calculations:
    for (int i = 0; i < n; i++) {
        if (level >= pairs[i][0] && level <= pairs[i][1]) {
            level++;
        }
    }

    // Output:
    printf("%d\n", level);

    // Free allocated memory:
    for (int i = 0; i < n; i++) {
        free(pairs[i]);
    }
    free(pairs);
    return 0;
}
