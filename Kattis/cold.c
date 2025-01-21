// https://open.kattis.com/problems/cold

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n;
    int* nums;
    scanf("%d", &n);
    nums = (int*)malloc(n * sizeof(int));
    int deg;
    for (int i = 0; i < n; i++) {
        scanf("%d", &deg);
        nums[i] = deg;
    }
    int lessThanZero = 0;
    for (int i = 0; i < n; i++) {
        if (nums[i] < 0) {
            lessThanZero++;
        }
    }
    printf("%d\n", lessThanZero);
    return 0;
}