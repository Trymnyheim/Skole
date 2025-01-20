// https://open.kattis.com/problems/dicegame

#include <stdio.h>

int main()
{
    int g[4];
    scanf("%d %d %d %d", &g[0], &g[1], &g[2], &g[3]);
    int e[4];
    scanf("%d %d %d %d", &e[0], &e[1], &e[2], &e[3]);
    int scoreG = 0;
    for (int i = 0; i < 4; i++) {
        scoreG += g[i];
    }
    int scoreE = 0;
    for (int i = 0; i < 4; i++) {
        scoreE += e[i];
    }

    if (scoreE > scoreG) {
        printf("Emma");
    }
    else if (scoreG > scoreE) {
        printf("Gunnar");
    }
    else {
        printf("Tie");
    }
}