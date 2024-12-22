// https://open.kattis.com/problems/echoechoecho

#include <stdio.h>

int main()
{
    char text[15];
    scanf("%s", text);
    printf("%s %s %s", &text, &text, &text);
    return 0;
}