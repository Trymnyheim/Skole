/*
 * Add the include files that you need. "man" can help you find them.
 * You will probably need stdio.h for printf and fprintf
 */
#include <stdio.h>
#include <string.h>

#include "vowelshift-todo.h"

/*
 * Find the requirements for these functions in the assignment text.
 */

int isVowel(char character)
{
    char vowels[] = "aeiouAEIOU";

    for (int i = 0; vowels[i] != '\0'; i++)
    {
        if (character == vowels[i])
        {
            return 1;
        }
    }

    return 0;
}

void vowelshift(char *buffer, char repl)
{
    for (int i = 0; buffer[i] != '\0'; i++)
    {
        if (isVowel(buffer[i]))
        {
            buffer[i] = repl;
        }
    }
}
