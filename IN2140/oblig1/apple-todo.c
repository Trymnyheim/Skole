/*
 * Add the include files that you need. "man" can help you find them.
 * You will probably need stdio.h for printf and fprintf
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "apple-todo.h"

/*
 * Find the requirements for these functions in the assignment text.
 */
int locateworm(char *buffer)
{
for (int i = 0; buffer[i] != '\0'; i++)
    {
        if (buffer[i] == 'w')
        {
            return i;
        }
    }
    return -1;
}

int removeworm(char *apple)
{
    int length = 0;

    int wormIndex = locateworm(apple);

    if (wormIndex == -1) {
	    return length;
    }

    apple += wormIndex * sizeof(char);

    while (*apple == 'w' || *apple == 'o' || *apple == 'r' || *apple == 'm')
    {
        *apple = ' ';
        length++;

        apple++;
    }

    return length;
}
