
/*
Implement constrained numbers, e.g. Num[1, 12].
*/

#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>

typedef struct num num;
struct num {
    uint64_t value;
    uint64_t min;
    uint64_t max;
};

num* new_num(uint64_t value, uint64_t min, uint64_t max) {
    if(min <= value && value <= max) {
        num *n = malloc(sizeof(num));
        n->min = min;
        n->max = max;
        n->value = value;
        return n;
    } else {
        puts("Value is out of range in constructor.");
        exit(1);
    }
}

void del_num(num *n) {
    free(n);
}

// Should constrained numbers error on bad values or silently constrain?
// n : Num[1, 10];
// n = 5;  # fine
// n = 15; # (exit) or (n==10)?

void main(void) {
    num *n = new_num(10, 15, 200);
    del_num(n);
}
