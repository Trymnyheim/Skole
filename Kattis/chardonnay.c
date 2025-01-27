// https://open.kattis.com/problems/chardonnay

#include <stdio.h>
#include <stdlib.h>

int* calcWine(int a){
    int *res = (int *)malloc(sizeof(int));
    if (res == NULL) {
        printf("Memory allocation faild.");
        return NULL;
    }
    if (a == 0) {
        *res = 0;
    }
    else if (a < 7) {
        *res = a + 1;
    }
    else {
        *res = a;
    }
    return res;
}

int main() {
    int *a = (int *)malloc(sizeof(int));
    if (a == NULL) {
        printf("Memory allocation faild.");
        return 1;
    }
    scanf("%d", a);
    int *res = calcWine(*a);
    printf("%d", *res);
    // Free memory
    free(a);
    free(res);
    return 0;
}