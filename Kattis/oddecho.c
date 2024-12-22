// https://open.kattis.com/problems/oddecho

#include <stdio.h>

int main()
{
    int n;
    scanf("%d", &n);
    char strings[n][100];

    for (int i = 0; i < n; i++) {
        scanf("%s", &strings[i]);
    }

    for (int i = 0; i < n; i++) {
        if ((i + 1) % 2 == 1) {
            printf("%s\n", &strings[i]);
        }
    }
    return 0;
}