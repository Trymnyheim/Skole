// https://open.kattis.com/problems/nodup

#include <stdio.h>
#include <string.h>

int main()
{
    char str[80];
    scanf("", str);
    char *word = strtok(str, " ");
    while (word != NULL) {
        printf("%s\n", word);
        word = strtok(NULL, " ");
    }

}