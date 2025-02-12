#ifndef STACK_H
#define STACK_H

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct Node {
    int value;
    struct Node* next;
};

struct Stack {
    struct Node* node;
};

struct Node* createNode(int nodeVal);
struct Stack* createStack();
void pushTo(struct Stack* stack, int val);
int popFrom(struct Stack* stack);
void freeStack(struct Stack* stack);
bool isNotEmpty(struct Stack* stack);

#endif