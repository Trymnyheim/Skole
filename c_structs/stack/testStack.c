#include "stack.h"

int main() {
    struct Stack* stack = createStack();
    pushTo(stack, 1);
    pushTo(stack, 2);
    pushTo(stack, 3);
    while (isNotEmpty(stack)) {
        printf("Value: %d\n", popFrom(stack));
    }
    return 0;
}