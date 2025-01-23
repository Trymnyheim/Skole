// https://open.kattis.com/problems/busassignment

#include <stdio.h>

int main()
{
    int n;
    scanf("%d", &n);
    int c = 0, amount = 0; // Max capacity, amount on bus
    int off, on;
    for (int i = 0; i < n; i++) {
        scanf("%d %d", &off, &on);
        amount = amount - off + on;
        if (amount > c) {
            c = amount;
        }
    }
    printf("%d", c);
    return 0;
}