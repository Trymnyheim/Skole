// https://open.kattis.com/problems/hairofthedog

#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main()
{
    int n;
    scanf("%d", &n);
    char word[10];
    int counter = 0;
    int cmp;
    bool isDrunk = false;
    for (int i = 0; i < n; i++) {
        scanf("%s", &word);
        cmp = strcmp(word, "drunk");
        if (cmp == 0) {
            if (!isDrunk) {
                counter++;
            }
            isDrunk = true;
        } else {
            isDrunk = false;
        }
    }
    printf("%d", counter);
    return 0;
}