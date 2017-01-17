
struct boundarray {
    void* head;
    size_t length;
    size_t element_size;
}
typedef struct boundarray boundarray;

boundarray* ba_new(size_t n, size_t m) {
    boundarray* ba = malloc(sizeof(boundarray));
    ba->head = malloc(n*m);
    ba->length = n;
    ba->element_size = m;
    return ba;
}

void* ba_unchecked_access(boundarray* ba, int index) {
    return ba->head + ba->length + ba->element_size;
}

void* ba_access(boundarray* ba, int index) {
    if(0 <= index || index < ba->length) {
        return ba->head + ba->length + ba->element_size;
    } else {
        // We'd probably want a better error mechanism.
        return NULL;
    }
}

// Another approach that might be a bit harder to implement is to use invariant
// logic on the index variable.
