// https://open.kattis.com/problems/modulo

#include <stdio.h>

int main()
{
    // Read input nums:
    int nums[10];
    for (int i = 0; i < 10; i++) {
        scanf("%d", &nums[i]);
    }

    // Init set:
    int set[42];
    for (int i = 0; i < 42; i++) {
        set[i] = -1;
    }

    // Make calculations:
    int counter = 10; // Max num of unique vals
    int mod;
    for (int i = 0; i < 10; i++) {
        mod = nums[i] % 42;
        if (set[mod] == -1) {
            set[mod] = mod; // Unique val
        } else {
            counter--;  // Non-unique val
        }
    }
    // Output:
    printf("%d", counter);
    return 0;
}