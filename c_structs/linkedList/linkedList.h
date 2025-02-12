#ifndef LINKEDLIST_H
#define LINKEDLIST_H

#include <stdio.h>
#include <stdlib.h>

struct Node {
    int value;
    struct Node* next;
};

struct LinkedList {
    struct Node* start;
    struct Node* current;
    struct Node* end;
};

struct Node* createNode(int nodeVal, struct Node* prev);
struct LinkedList* newLinkedList();
void addToList(struct LinkedList* linkedList, int newVal);
struct Node* fromStart(struct LinkedList* linkedList);
struct Node* nextInList(struct LinkedList* linkedList);
void freeList(struct LinkedList* linkedList);

#endif