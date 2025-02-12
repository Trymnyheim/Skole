#ifndef HASHSET_H
#define HASHSET_H

#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

struct HashSet {
    char** values;
    int size;
    int amount;
};

int hash(char* val, int size);
struct HashSet* newSet(int size);
bool contains(struct HashSet* hashSet, char* val);
struct HashSet* addTo(struct HashSet* hashSet, char* val);
void removeFrom(struct HashSet* hashSet, char* val);
struct HashSet* reHash(struct HashSet* hashSet);
void freeHashSet(struct HashSet* hashSet);

#endif