typedef enum {
    N_INT = 2048,
    N_IDENTIFIER,
    N_EXPRESSION,
    N_STATEMENT,
    N_FLOAT,
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

#define CHILD_LENGTH 128

typedef struct {
    int type;
    int lineno;
    char *value;
}Node_const;

typedef struct {
    int type;
    int lineno;
    int op;
    
    Node_const *left;
    Node_const *right;
}Node_op;


typedef struct {
    int type;
    char *value;
    int lineno;
}Node_identifier;

typedef struct {

}Node_variable;