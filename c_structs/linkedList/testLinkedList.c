#include "linkedList.h"

int main() {
    struct LinkedList* linkedList = newLinkedList();
    addToList(linkedList, 1);
    addToList(linkedList, 2);
    addToList(linkedList, 3);
    struct Node* node = fromStart(linkedList);
    while (node != NULL) {
        printf("Value: %d\n", node->value);
        node = nextInList(linkedList);
    }
    freeList(linkedList);
    return 0;
}