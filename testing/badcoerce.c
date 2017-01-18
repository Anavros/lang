
// What happens when you coerse one struct to another, when they have nothing
// in common?

#include <stdlib.h>

typedef struct A A;
typedef struct B B;

struct A {
    int a, b, c;
};

struct B {
    char x;
    float u, v;
};

void main(void) {
    A *a = malloc(sizeof(A));
    B *b = (B*)a;
}

// Absolutely nothing apparently.
// C really isn't very strongly typed is it.
// Which is good for language design I guess.
