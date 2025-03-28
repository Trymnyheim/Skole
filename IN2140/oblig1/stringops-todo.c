/*
 * Add the include files that you need. "man" can help you find them.
 * You will probably need stdio.h for printf and fprintf
 */
#include <stdio.h>
#include <string.h>

#include "stringops-todo.h"

/*
 * Find the requirements for these functions in the assignment text.
 */
int stringsum(char *s)
{
    int result = 0;

    for (int i = 0; s[i] != '\0'; i++)
    {
        if (s[i] >= 'A' && s[i] <= 'Z')
        {
            result += s[i] - ('A' - 1);
        }
        else if (s[i] >= 'a' && s[i] <= 'z')
        {
            result += s[i] - ('a' - 1);
        }
        else if (s[i] != ' ')
        {
            return -1;
        }
    }

    return result;
}

int distance_between(char *s, char c)
{
    int firstIndex = -1;
    int lastIndex = -1;

    for (int i = 0; s[i] != '\0'; i++)
    {
        if (s[i] == c && firstIndex == -1)
        {
            firstIndex = i;
        }
        else if (s[i] == c)
        {
            lastIndex = i;
        }
    }

    if (firstIndex == -1)
        return -1;
    else if (lastIndex == -1)
        return 0;
    return lastIndex - firstIndex;
}

char *string_between(char *s, char c)
{
    int distance = distance_between(s, c);

    if (distance == -1)
    {
        return NULL;
    }

    while (*s != '\0' && *s != c)
    {
        s++;
    }

    // Result is now the adress of the first occurence of c
    char *result = s;

    // Increasing by 1 makes result point to the character after c, if we want
    // the array of characters _between_ the first and last occurence of c.
    if (distance != 0)
    {
        result++;
    }

    s += distance;

    *s = '\0';

    return result;
}

int stringsum2(char *s, int *res)
{
    int sum = stringsum(s);
    *res = sum;

    int exitcode = 0;
    if (sum <= 0)
    {
        exitcode = sum;
    }

    return exitcode;
}
