// https://open.kattis.com/problems/countthevowels

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <ctype.h>

bool isVowel(char letter) {
    char *vowels = "aeiou";
    for (int i = 0; i < strlen(vowels); i++) {
        if (tolower(letter) == vowels[i]) {
            return true;
        }
    }
    return false;
}

int main() {
    char *string = (char *)malloc(81 * sizeof(char));
    if (string == NULL) {
        fprintf(stderr, "Failed to allocate memory for string.");
        return 1;
    }
    fgets(string, 81, stdin);
    string[strcspn( string, "\n" )] = '\0';

    int vowelCount = 0;
    for (int i = 0; i < strlen(string); i++) {
        if(isVowel(string[i])) {
            vowelCount++;
        }
    }
    printf("%d", vowelCount);
    free(string);
    return 0;
}