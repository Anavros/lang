
// ???

struct boundedarray {
    char* elements;
    size_t len;
};
typedef struct boundedarray barr;

struct pair {
    char a;
    char b;
}
typedef struct pair pair;

struct iterator {
}

struct iterpair {
}

// Allocates on the heap; must free afterwards!
barr* new_barr(size_t len) {
    new = malloc(sizeof barr);
    new->len = len;
    new->elements = malloc(len);
    return new;
}

barr* zip(barr* a, barr* b) {
    // assuming all barrs are char arrays
    if(a->len != b->len) {
        return NULL;
    }
    barr* zipped = new_barr(a->len);
}
