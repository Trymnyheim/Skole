#include "hashSet.h"

int main() {
    struct HashSet* hashSet = newSet(10);
    hashSet = addTo(hashSet, "Trym");
    hashSet = addTo(hashSet, "Per");
    hashSet = addTo(hashSet, "Ingvild");
    hashSet = addTo(hashSet, "Tor");
    hashSet = addTo(hashSet, "Trude");
    hashSet = addTo(hashSet, "Kåre");
    hashSet = addTo(hashSet, "Peder");
    hashSet = addTo(hashSet, "Kari");
    if (contains(hashSet, "Kari")) {
        printf("Ja\n");
    } else {
        printf("Nei\n");
    }
    printf("%d\n", hashSet->size);
    freeHashSet(hashSet);
    return 0;
}