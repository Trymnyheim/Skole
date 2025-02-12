#include "Stack.h"
#include <limits.h>

struct Node* createNode(int nodeVal) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    if (newNode == NULL) {
        fprintf(stderr, "Error allocating memory for new stack.");
        exit(-1);
    }
    newNode->value = nodeVal;
    newNode->next = NULL;
    return newNode;
}

struct Stack* createStack() {
    struct Stack* stack = (struct Stack*)malloc(sizeof(struct Stack));
    if (stack == NULL) {
        fprintf(stderr, "Error allocating memory for new stack.");
        exit(-1);
    }
    stack->node = NULL;
    return stack;
}

void pushTo(struct Stack* stack, int val) {
    struct Node* node = createNode(val);
    if (stack->node != NULL) {
        node->next = stack->node;
    }
    stack->node = node;
}

int popFrom(struct Stack* stack) {
    struct Node* node = stack->node;
    if (node == NULL) {
        return INT_MIN;
    }
    int val = node->value;
    stack->node = node->next;
    free(node);
    return val;
}

void freeStack(struct Stack* stack) {
    struct Node* node = stack->node;
    while (node != NULL) {
        stack->node = node->next;
        free(node);
        node = stack->node;
    }
    free(stack);
}

bool isNotEmpty(struct Stack* stack) {
    if (stack->node == NULL) {
        return false;
    }
    return true;
}