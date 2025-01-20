// https://open.kattis.com/problems/pyramids

#include <stdio.h>

int main()
{
    int n;
    scanf("%d", &n);
    int size = 0;
    int width = 1;
    int level = 0;
    while (size <= n) {
        level++;
        size += width * width;
        width += 2;
    }
    level--;
    printf("%d\n", level);
}