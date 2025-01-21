// https://open.kattis.com/problems/hipphipphurra

#include <stdio.h>

int main()
{
    char name[50];
    int age;
    scanf("%s", &name);
    scanf("%d", &age);
    for (int i = 0; i < age; i++) {
        printf("Hipp hipp hurra, %s!\n", name);
    }
    return 0;
}