// https://open.kattis.com/problems/takkfyrirmig

#include <stdio.h>

int main()
{
    int n;
    scanf("%d", &n);
    char names[n][50];
    for (int i = 0; i < n; i++) {
        scanf("%s", &names[i]);
    }
    for (int i = 0; i < n; i++) {
        printf("Takk %s\n", names[i]);
    }
}