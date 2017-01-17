
#include <stdlib.h>
#include <stdio.h>

#define TYPE_INT 0
#define TYPE_FLOAT 1

typedef struct dyntype dyntype;

struct dyntype {
    int id;
    void (*print)(dyntype*);
};

typedef struct {
    dyntype* type;
    int value;
} dint;

typedef struct {
    dyntype* type;
    float value;
} dfloat;

void dint_print(dyntype* d) {
    dint* i = (dint*)d;
    printf("Dynamic Int: %d\n", i->value);
}

void dfloat_print(dyntype* d) {
    dfloat* f = (dfloat*)d;
    printf("Dynamic Float: %f\n", f->value);
}

dyntype* new(int type) {
    dyntype *t = malloc(sizeof(dyntype));
    switch(type) {
        case(TYPE_INT):;
            dint *i = malloc(sizeof(dint));
            t->id = TYPE_INT;
            t->print = dint_print;
            i->type = t;
            i->value = 0;
            return (dyntype*)i;

        case(TYPE_FLOAT):;
            dfloat *f = malloc(sizeof(dfloat));
            t->id = TYPE_FLOAT;
            t->print = dfloat_print;
            f->type = t;
            f->value = 0.0;
            return (dyntype*)f;

        default:
            return NULL;
    }
}

void destroy(dyntype *d) {
    switch(d->id) {
        case(TYPE_INT):;
            dint* i = (dint*)d;
            free(i->type);
            free(i);
        case(TYPE_FLOAT):;
            dfloat* f = (dfloat*)d;
            free(f->type);
            free(f);
        default:;
            free(d);
    }
}

void main(void) {
    dyntype *ad = new(TYPE_FLOAT);
    dfloat *af = (dfloat*)ad;
    dyntype *bd = new(TYPE_INT);
    dint *bi = (dint*)bd;
    af->type->print(ad);
    bi->type->print(bd);
    destroy(ad);
    destroy(bd);
}
