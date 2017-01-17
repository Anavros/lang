
#include <stdlib.h>
#include <stdio.h>

/*
Create two structures, A and B, where B contains all members of A, and more.
Design a function that will accept either A or B, and only use the members
present in A.
*/

typedef struct {
    int x, y, z;
} A;

typedef struct {
    int x, y, z;
    char a, b, c;
} B;

// Requires struct A.
int xyz_sum(A* aptr) {
    A a = *aptr;
    return (a.x+a.y+a.z);
}

void main(void) {
    A* a = malloc(sizeof(A));
    a->x = 1;
    a->y = 2;
    a->z = 3;
    int a_total = xyz_sum(a);
    printf("Total of struct A: %d\n", a_total);
    free(a);

    B* b = malloc(sizeof(B));
    b->x = 1;
    b->y = 2;
    b->z = 3;
    b->a = 'f';
    b->b = 'g';
    b->c = 'h';
    // Notice that B* has to be coerced to A*.
    int b_total = xyz_sum((A*)b);
    printf("Total of struct B: %d\n", b_total);
    free(b);
}
