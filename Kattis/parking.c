// https://open.kattis.com/problems/parking2

#include <stdio.h>

int find()
{
    int n;
    scanf("%d", &n);
    int min = 100;
    int max = 0;
    int x;
    for (int i = 0; i < n; i++) {
        scanf("%d", &x);
        if (x < min) {
            min = x;
        }
        if (x > max) {
            max = x;
        }
    }
    int res = (max - min) * 2;
    return res;
}

int main()
{
    int cases;
    scanf("%d", &cases);
    int outputs[cases];
    for (int i = 0; i < cases; i++) {
        int res = find();
        outputs[i] = res;
    }
    
    for (int i = 0; i < cases; i++) {
        printf("%d\n", outputs[i]);
    }
    return 0;
}