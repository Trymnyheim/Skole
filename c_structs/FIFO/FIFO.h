#ifndef FIFO_H
#define FIFO_H

#include <stdio.h>
#include <stdlib.h>

struct Node {
    int value;
    struct Node* prev;
};

struct FIFO {
    struct Node* first;
    struct Node* last;
};

struct Node* createNode(int value);
struct FIFO* createFIFO();
void insertTo(struct FIFO* queue, int value);
int removeFrom(struct FIFO* queue);
void freeFIFO(struct FIFO* queue);

#endif