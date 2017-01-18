
/*
Virtual Machine
Read a series of opcodes and dispatch appropriate c code.
*/

#include <stdlib.h>
#include <stdio.h>

#define FILEPATH "input.malt"
#define MALT_MAX_NUM_TOKENS 2048

#define MALT_TOKEN_PRINT 0
#define MALT_TOKEN_END_STATEMENT 1
#define MALT_TOKEN_EOF   2
#define MALT_TOKEN_HALT  3


void opcode_print(void) {
    puts("Print!");
}


// Load a file into memory as a long string of chars, ending with \0.
// Returns NULL on failure.
char* load_file(char *filepath) {
    FILE *f = fopen(filepath, "r");
    if (!f) return NULL;
    fseek(f, 0, SEEK_END);
    long len = ftell(f);
    fseek(f, 0, SEEK_SET);
    char *buffer = malloc(len+1);
    if (!buffer) return NULL;
    fread(buffer, 1, len, f);
    buffer[len] = '\0';
    fclose(f);
    return buffer;
}

// Iterate over the file in memory and generate a list of tokens.
int* parse(char *file) {
    // File guaranteed not to be NULL by caller.
    // How long to make the buffer?
    int *tokens = malloc(sizeof(int)*MALT_MAX_NUM_TOKENS);
    if(!tokens) return NULL;
    // Temp obviously.
    tokens[0] = MALT_TOKEN_PRINT;
    tokens[1] = MALT_TOKEN_PRINT;
    tokens[2] = MALT_TOKEN_EOF;
    tokens[3] = MALT_TOKEN_HALT;
    return tokens;
}

void execute(int *tokens) {
    int i = 0;
    int t = tokens[i];
    while(t != MALT_TOKEN_HALT) {
        printf("Token [%d]\n", t);
        i++;
        t = tokens[i];
    }
    puts("Execution finished.");
}

int main(void) {
    char *buffer = load_file(FILEPATH);
    if(buffer == NULL) {
        puts("Buffer is NULL, abort.");
        return 1;
    }
    int* tokens = parse(buffer);
    if(tokens == NULL) {
        puts("Tokens is NULL, abort.");
        return 1;
    }
    execute(tokens);
    free(buffer);
    free(tokens);
    return 0;
}
