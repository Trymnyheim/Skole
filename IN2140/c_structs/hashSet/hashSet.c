#include "hashSet.h"

int hash(char* val, int size) {
    int hash = 0;
    for (int i = 0; val[i] != '\0'; i++) {
        hash = (int)val[i] + (31 * hash);
    }
    return (hash & 0x7FFFFFFF) % size;
}

struct HashSet* newSet(int size) {
    struct HashSet* hashSet = (struct HashSet*)malloc(sizeof(struct HashSet));
    if (hashSet == NULL) {
        fprintf(stderr, "Failed to allocate memory for HashSet.");
        exit(-1);
    }
    hashSet->size = size;
    hashSet->amount = 0;
    hashSet->values = (char**)malloc(size * sizeof(char*));
    if (hashSet->values == NULL) {
        fprintf(stderr, "Failed to allocate memory for HashSet.");
        exit(-1);
    }
    for (int i = 0; i < size; i++) {
        hashSet->values[i] = NULL;
    }
    return hashSet;
}

bool contains(struct HashSet* hashSet, char* val) {
    int hashVal = hash(val, hashSet->size);
    int i = hashVal;
    while (hashSet->values[i] != NULL) {
        if(strcmp(hashSet->values[i], val) == 0) {
            return true;
        }
        i = (i + 1) % hashSet->size;
        if (i == hashVal) {
            return false;
        }
    }
    return false;
}

struct HashSet* addTo(struct HashSet* hashSet, char* val) {
    int hashVal = hash(val, hashSet->size);
    int i = hashVal;
    while (hashSet->values[i] != NULL) {
        if (strcmp(hashSet->values[i], val) == 0) {
            return hashSet;
        }
        i = (i + 1) % hashSet->size;
        if (i == hashVal) {
            fprintf(stderr, "Error: HashMap is full.");
            exit(-1);
        }
    }
    hashSet->values[i] = val;
    hashSet->amount++;
    return reHash(hashSet);
}


void removeFrom(struct HashSet* hashSet, char* val) {
    int hashVal = hash(val, hashSet->size);
    int i = hashVal;
    while (hashSet->values[i] != NULL) {
        if (strcmp(hashSet->values[i], val) == 0) {
            hashSet->values[i] = NULL;
        }
        i = (i + 1) % hashSet->size;
    }
    i = (i + 1) % hashSet->size;
    while (hashSet->values[i] != NULL) {
        val = hashSet->values[i];
        hashSet->values[i] = NULL;
        addTo(hashSet, val);
        i = (i + 1) % hashSet->size;

    }
    hashSet->amount--;
}

struct HashSet* reHash(struct HashSet* hashSet) {
    float density = (float)hashSet->amount/hashSet->size;
    if (density < 0.7) {
        return hashSet;
    }
    int newSize = hashSet->size * 2;
    struct HashSet* newHashSet = newSet(newSize);
    for (int i = 0; i < hashSet->size; i++) {
        if (hashSet->values[i] != NULL) {
            addTo(newHashSet, hashSet->values[i]);
        }
    }
    freeHashSet(hashSet);
    return newHashSet;
}

void freeHashSet(struct HashSet* hashSet) {
    free(hashSet->values);
    free(hashSet);
}
