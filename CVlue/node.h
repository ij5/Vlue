typedef enum {
    N_INT = 2048,
    N_IDENTIFIER,
    N_EXPRESSION,
    N_STATEMENT,
    N_INT,
    N_ADD,
    N_SUB,
    N_MUL,
    N_DIV,
    N_LSB,
    N_RSB,
    N_EQUAL,
    N_VAR,
    N_NEWLINE,
    N_DECLARATION,
}NodeType;

typedef struct _Node{
    int type;
    int lineno;

    char *value;
    struct _Node children[128];
}Node;