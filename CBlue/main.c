#include <stdio.h>
#define OWL_PARSER_IMPLEMENTATION
#include "parser.h"

int main(void){
    struct owl_tree *tree;
    tree = owl_tree_create_from_file(stdin);
    owl_tree_print(tree);
    owl_tree_destroy(tree);
    return 0;
}
