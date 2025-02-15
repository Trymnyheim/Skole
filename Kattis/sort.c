#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Number {
    char* num;
    int freq;
};

int findNumber(struct Number* nums, char* target, int amount) {
    for (int i = 0; i < amount; i++) {
        if (strcmp(nums[i].num, target) == 0) {
            return i;
        }
    }
    return amount;
}

void sortNumsByFreq(struct Number* nums, int amount) {
    for (int i = 1; i < amount; i++) {
        struct Number current = nums[i];
        int j = i - 1;

        // Find the correct position for 'current' in the sorted portion
        while (j >= 0 && nums[j].freq < current.freq) {
            nums[j + 1] = nums[j];  // Shift element to the right
            j--;
        }
        
        // Insert the element at its correct position
        nums[j + 1] = current;
    }
}

int main() {
    // Read parameters:
    char buffer[30];
    if (fgets(buffer, sizeof(buffer), stdin) == NULL) {
        fprintf(stderr, "Error reading input\n");
        return 1;
    }

    int n, c;
    if (sscanf(buffer, "%d %d", &n, &c) != 2) {
        fprintf(stderr, "Invalid input format\n");
        return 1;
    }

    // Read input
    char* line = NULL;
    size_t bufsize = 0;
    ssize_t length = getline(&line, &bufsize, stdin);
    if (length == -1) {
        fprintf(stderr, "Error reading input line\n");
        return 1;
    }

    // Allocate space for number structs:
    struct Number* nums = (struct Number *)malloc(n * sizeof(struct Number));
    if (!nums) {
        fprintf(stderr, "Memory allocation failed\n");
        free(line);
        return 1;
    }

    // Read and process numbers:
    int amount = 0;
    char strInt[15];
    int strIndex = 0;
    for (int i = 0; i < length; i++) {
        if (line[i] != ' ' && line[i] != '\n') {
            strInt[strIndex++] = line[i];
        } else {
            strInt[strIndex] = '\0';
            strIndex = 0;
            // Process and update numbers:
            int numberIndex = findNumber(nums, strInt, amount);
            if (numberIndex == amount) {
                struct Number number;
                number.num = strdup(strInt);
                number.freq = 1;
                nums[numberIndex] = number;
                amount++;
            }
            else {
                nums[numberIndex].freq++;
            }
        }
    }
    free(line);

    // Sort by frequency:
    sortNumsByFreq(nums, amount);

    for (int i = 0; i < n; i++) {
        while (nums[i].freq != 0) {
            printf("%s ", nums[i].num);
            nums[i].freq--;
        }
        free(nums[i].num); // Free allocated string
    }

    free(nums);

    return 0;
}