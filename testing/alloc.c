
#include <stdlib.h>

void main(void) {
    // Allocate 4 bytes.
    char *c = malloc(4);
    // And free it immediately.
    free(c);
}
