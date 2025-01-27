// https://open.kattis.com/problems/whichnumberkindisit2

#include <stdio.h>
#include <stdbool.h>
#include <math.h>
#include <stdlib.h>

bool isOdd(int n) {
    if (n % 2 == 1) {
        return true;
    }
    return false;
}

bool isSquare(int n) {
    if (sqrt(n) == (int) sqrt(n)) {
        return true;
    }
    return false;
}

int main() {
    int *cases = (int *)malloc(sizeof(int));
    if (cases == NULL) {
        fprintf(stderr, "Error allocating memory");
        return 1;
    }
    // Read amount of cases:
    scanf("%d", cases);

    // Allocate for nums:
    int *nums = (int *)malloc(*cases * sizeof(int));
    if (nums == NULL) {
        fprintf(stderr, "Error allocating memory");
        return 1;
    }

    // Read input:
    for (int i = 0; i < *cases; i++) {
        scanf("%d", &nums[i]);
    }

    // Find number kind and give output:
    for (int i = 0; i < *cases; i++) {
        if (isOdd(nums[i]) || isSquare(nums[i])) {
            if (isOdd(nums[i])){
                printf("O");
            }
            if (isSquare(nums[i])) {
                printf("S");
            }
            printf("\n");
        }
        else {
            printf("EMPTY\n");
        }
    }
    
    // Free allocated memory:
    free(cases);
    free(nums);

    return 0;
}