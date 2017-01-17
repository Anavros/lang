
#include <stdlib.h>
#include <stdio.h>

#define MALT_TYPE_INT 0
#define MALT_TYPE_FLOAT 1

struct MaltType {
    int value;
};
typedef struct MaltType MaltType;

struct PointInt {
    MaltType *type;
    int x, y, z;
};
typedef struct PointInt PointInt;

struct PointFloat {
    MaltType *type;
    float x, y, z;
};
typedef struct PointFloat PointFloat;

struct MaltInt {
    MaltType *type;
    int value;
};
typedef struct MaltInt MaltInt;

struct MaltFloat {
    MaltType *type;
    float value;
};
typedef struct MaltFloat MaltFloat;

int unbox_int(MaltInt* i) {
    return i->value;
}

float unbox_float(MaltFloat* f) {
    return f->value;
}

MaltType* new_point(int type) {
    MaltType *tstruct = malloc(sizeof(MaltType));
    PointInt *pi;
    PointFloat *pf;
    switch(type) {
        case(MALT_TYPE_INT):
            pi = malloc(sizeof(PointInt));
            tstruct->value = MALT_TYPE_INT;
            pi->type = tstruct;
            pi->x = pi->y = pi->z = 0;
            return (MaltType*)pi;
        case(MALT_TYPE_FLOAT):
            pf = malloc(sizeof(PointFloat));
            tstruct->value = MALT_TYPE_FLOAT;
            pf->type = tstruct;
            pf->x = pf->y = pf->z = 0.0;
            return (MaltType*)pf;
        default:
            return NULL;
    }
}

MaltType* point_sum(MaltType *point) {
    MaltInt *i;
    MaltFloat *f;
    switch(point->value) {
        case(MALT_TYPE_INT):
            i = malloc(sizeof(MaltInt));
            PointInt *pi = (PointInt*)point;
            i->value = pi->x + pi->y + pi->z;
            return (MaltType*)i;
        case(MALT_TYPE_FLOAT):
            f = malloc(sizeof(MaltFloat));
            PointFloat *pf = (PointFloat*)point;
            f->value = pf->x + pf->y + pf->z;
            return (MaltType*)f;
        default:
            return NULL;
    }
}

void main(void) {
    PointInt* ip = (PointInt*)new_point(MALT_TYPE_INT);
    PointFloat* fp = (PointFloat*)new_point(MALT_TYPE_FLOAT);
    ip->x = 1;
    ip->y = 2;
    ip->z = 3;
    int total = unbox_int((MaltInt*)point_sum((MaltType*)ip));
    printf("%i\n", total);
    free(ip);
    free(fp);
}
