#include "linkedList.h"

struct Node* createNode(int nodeVal, struct Node* prev) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    if (newNode == NULL) {
        fprintf(stderr, "Failed to allocate memory for new node.");
        exit(-1);
    }
    if (prev != NULL) {
        prev->next = newNode;
    }
    newNode->value = nodeVal;
    newNode->next = NULL;
    return newNode;
}

struct LinkedList* newLinkedList() {
    struct LinkedList* newList = (struct LinkedList*)malloc(sizeof(struct LinkedList));
    if (newList == NULL) {
        fprintf(stderr, "Failed to allocate memory for new list.");
        exit(-1);
    }
    newList->start = NULL;
    newList->current = NULL;
    newList->end = NULL;
    return newList;
}

void addToList(struct LinkedList* linkedList, int newVal) {        
    linkedList->end = createNode(newVal, linkedList->end);
    if (linkedList->start == NULL) {
        linkedList->start = linkedList->end;
    }
}

struct Node* fromStart(struct LinkedList* linkedList) {
    linkedList->current = linkedList->start;
    return linkedList->current;
}

struct Node* nextInList(struct LinkedList* linkedList) {
    if (linkedList->current != NULL) {
        linkedList->current = linkedList->current->next;
    }
    return linkedList->current;
}

void freeList(struct LinkedList* linkedList) {
    struct Node* node = linkedList->start;
    struct Node* next;
    while (node != NULL) {
        next = node->next;
        free(node);
        node = next;
    }
    free(linkedList);
}