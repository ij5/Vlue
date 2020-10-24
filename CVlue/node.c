#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "node.h"

#define TOKEN_LENGTH 1024

Node_op *create_node_op(int type, int op, Node_const *left, Node_const *right, int lineno){
    Node_op *node = malloc(sizeof(Node_op));
    node->type = type;
    node->op = op;
    node->lineno = lineno;
    node->left = left;
    node->right = right;
}

Node_const *create_node_const(int type, char *value, int lineno){
    Node_const *node = malloc(sizeof(Node_const));
    node->type = type;
    node->value = malloc(sizeof(char) * TOKEN_LENGTH);
    strcpy(node->value, value);
    node->lineno = lineno;
}

Node_identifier *create_node_identifier(int type, char *value, int lineno){
    Node_identifier *node = malloc(sizeof(Node_identifier));
    node->type = type;
    node->value = malloc(sizeof(char) * TOKEN_LENGTH);
    strcpy(node->value, value);
    node->lineno = lineno;
}