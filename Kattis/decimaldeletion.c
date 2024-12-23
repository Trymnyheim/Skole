// https://open.kattis.com/problems/decimaldeletion

#include <stdio.h>

int main()
{
    double n;
    scanf("%lf", &n);
    n = n + 0.5;
    int x = (int)n;
    printf("%d\n", x);
    return 0;
}