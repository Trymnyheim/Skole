// https://open.kattis.com/problems/quadrant

#include <stdio.h>

int main()
{
    int x;
    int y;
    scanf("%d", &x);
    scanf("%d", &y);
    int quad;
    if (x >= 0) {
        if (y >= 0) {
            quad = 1;
        } else {
            quad = 4;
        }
    }
    else {
        if (y >= 0) {
            quad = 2;
        } else {
            quad = 3;
        }
    }
    printf("%d\n", quad);
    return 0;
}