#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "node.h"

#define TOKEN_LENGTH 1024

Node create_node(int type, char *value, int lineno){
    Node *node = malloc(sizeof(Node));
    node->type = type;
    node->value = malloc(sizeof(TOKEN_LENGTH));
    strcpy(node->value, value);
    node->lineno = lineno;
}

void free_node(Node *node){
    free(node->value);
    free(node);
}