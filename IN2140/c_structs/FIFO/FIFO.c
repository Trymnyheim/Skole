#include "FIFO.h"

struct Node* createNode(int value) {
    struct Node* node = (struct Node*)malloc(sizeof(struct Node));
    if (node == NULL) {
        fprintf(stderr, "Error allocating memory for new node.");
        exit(-1);
    }
    node->value = value;
    node->prev = NULL;
    return node;
}
struct FIFO* createFIFO() {
    struct FIFO* queue = (struct FIFO*)malloc(sizeof(struct FIFO));
    if (queue == NULL) {
        fprintf(stderr, "Error allocating memory for new FIFO queue.");
        exit(-1);
    }
    queue->first = NULL;
    queue->last = NULL;
    return queue;
}
void insertTo(struct FIFO* queue, int value) {
    struct Node* node = createNode(value);
    if (queue->first == NULL) {
        queue->last = node;
    } else {
        queue->first->prev = node;
    }
    queue->first = node;
}

int removeFrom(struct FIFO* queue) {
    if (queue->last == NULL) {
        return -1;
    }
    struct Node* node = queue->last;
    int value = node->value;
    queue->last = node->prev;
    if (queue->last == NULL) {
        queue->first = NULL;
    }
    free(node);
    return value;
}

void freeFIFO(struct FIFO* queue) {
    struct Node* node = queue->last;
    struct Node* prev;
    while (node != NULL) {
        prev = node->prev;
        free(node);
        node = prev;
    }
    free(queue);
}