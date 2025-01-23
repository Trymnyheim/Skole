// https://open.kattis.com/problems/baconeggsandspam

#include <stdio.h>

int main()
{
    int n;
    scanf("%d", &n);
    while (n != 0) {
        char name[15];
        char food[15];
        scanf("%s %s", &name, &food);
        printf("%s", name);





        scanf("%d", &n); // Next case size
    }
    return 0;
}