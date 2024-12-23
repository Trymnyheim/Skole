// https://open.kattis.com/problems/isyavowel

#include <stdio.h>
#include <string.h>

int main()
{
    char letters[50];
    scanf("%s", &letters);
    char vowels[] = "aeiou";
    int withoutY = 0;
    int withY = 0;
    for (int i = 0; i < strlen(letters); i++) {
        char letter = letters[i];
        if (strchr(vowels, letter)) {
            withY++;
            withoutY++;
        }
        else if (letter == 'y') {
            withY++;
        }
    }
    printf("%d %d\n", withoutY, withY);
}