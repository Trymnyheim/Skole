// https://open.kattis.com/problems/pet

#include <stdio.h>
#include <stdlib.h>

int main() {
    // Allocate memory for scores:
    int **res = (int **)malloc(5 * sizeof(int *));
    if (res == NULL) {
        return 1;
    }
    for (int i = 0; i < 5; i++) {
        res[i] = (int *)malloc(4 * sizeof(int));
        if (res[i] == NULL) {
            fprintf(stderr, "Error allocating memory for res[%d]", i);
            return 1;
        }
    }

    // Read input:
    for (int i = 0; i < 5; i++) {
        scanf("%d %d %d %d", &res[i][0], &res[i][1], &res[i][2], &res[i][3]);
    }

    // Find max:
    int max = 0;
    int max_val = 0;
    for (int i = 0; i < 5; i++) {
        int val = 0;
        for (int j = 0; j < 4; j++) {
            val += res[i][j];
        }
        if (val > max_val) {
            max = i + 1;
            max_val = val;
        }
    }

    // Output result:
    printf("%d %d\n", max, max_val);

    // Free allocated memory:
    for (int i = 0; i < 5; i++) {
        free(res[i]);
    }
    free(res);
    return 0;
}