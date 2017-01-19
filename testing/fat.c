
// Implement fat pointer structs. Aka sized arrays.

typedef struct iarray iarray;
typedef struct carray carray;

struct iarray {
    size_t size;
    int *pointer;
}

struct carray {
    size_t size;
    char *pointer;
}

size_t fatstrlen(carray *string) {
    return string->size;
}

char *getstr(carray *string) {
    return string->pointer;
}

carray* fatstrcopy(carray *old) {
    size_t size = old->size;
    char *oldstring = old->pointer;
    char *newstring = malloc(size);
    for(int i=0; i<size; i++) {
        newstring[i] = oldstring[i];
    }
    carray *new = malloc(sizeof(carray));
    new->size = size;
    new->pointer = newstring;
    return new;
}
