#include "FIFO.h"

int main() {
    struct FIFO* queue = createFIFO();
    insertTo(queue, 1);
    insertTo(queue, 2);
    insertTo(queue, 3);
    printf("Value: %d\n", removeFrom(queue));
    printf("Value: %d\n", removeFrom(queue));
    printf("Value: %d\n", removeFrom(queue));
    freeFIFO(queue);
    return 0;
}