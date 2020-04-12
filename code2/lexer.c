#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

enum Lexicon {WHITESPACE, IDENTIFIER, PLUS, LEFT_BRACE, RIGHT_BRACE, END};

struct Token {
    enum Lexicon lex;
    const char *str;
    size_t len;
};

struct Token lexer(const char **str) {
    struct Token token;
    if (**str== '+') {
        token.lex= PLUS;
        token.str = *str;
        token.len = 1;
        ++*str;
    } else if (**str == '(') {
        token.lex= LEFT_BRACE;
        token.str = *str;
        token.len = 1;
        ++*str;
    } else if (**str == ')') {
        token.lex= RIGHT_BRACE;
        token.str = *str;
        token.len = 1;
        ++*str;
    } else if (isspace(**str)) {
        token.lex= WHITESPACE;
        token.str = *str;
        token.len = 1;
        ++*str;
    } else if (isalpha(**str)) {
        token.lex = IDENTIFIER;
        token.str = *str;
        token.len = 0;
        while (isalpha(**str)) {
            ++token.len;
            ++*str;
        }
    }else {
        printf("lexer error at : %s \n", *str);
        exit(0);
    }
    return token;
}

enum Syntax {SYN_EXPRESSION, SYN_PLUS, SYN_CALL, SYN_IDENTIFIER};

struct AbstractSyntaxTree {
    enum Syntax syn;
    struct AbstractSyntaxTree* left;
    struct AbstractSyntaxTree* right;
    const char *data;
};

struct AbstractSyntaxTree* expr2(struct Token **t);
struct AbstractSyntaxTree* expr1_prime(struct Token **t);
struct AbstractSyntaxTree* parser(struct Token **t); //expr1

struct AbstractSyntaxTree* expr3(struct Token **t)
{
    struct AbstractSyntaxTree* node = malloc(sizeof(*node));
    if ((*t)->lex == IDENTIFIER) {
        if ((*t)->len == 1) {
            char *data = malloc((*t)->len+1);
            strncpy(data, (*t)->str, (*t)->len);
            data[(*t)->len] = '\0';
            ++*t; // matching identifier
            node->left = NULL;
            node->right = NULL;
            node->syn = SYN_IDENTIFIER;
            node->data = data;
        } else {
            printf("error : variable can be a one letter.\n");
            exit(0);
        }
    } else {
        printf("syntax error(3) : not a identifier. \n");
        exit(0);
    }
    return node;
}

struct AbstractSyntaxTree* expr2(struct Token **t)
{
    struct AbstractSyntaxTree* node = malloc(sizeof(*node));
    if ((*t)->lex == IDENTIFIER) {
        if ( ((*t)+1)->lex == LEFT_BRACE) {
            char *data = malloc((*t)->len+1);
            strncpy(data, (*t)->str, (*t)->len);
            data[(*t)->len] = '\0';
            ++*t; // matching 'identifier'
            ++*t; // matching '['
            node->left = parser(t); // expr1
            node->right = NULL;
            node->data = data;
            node->syn = SYN_CALL;
        } else {
            free(node);
            node = expr3(t);
        }
    } else {
        printf("syntax error(2) : not a identifier nor calling expression.\n");
        exit(0);
    }
    return node;
}

struct AbstractSyntaxTree* expr1_prime(struct Token **t)
{
    struct AbstractSyntaxTree* node = malloc(sizeof(*node));
    if ((*t)->lex == PLUS) {
        ++*t; // match
        node->left = expr2(t);
        node->right = expr1_prime(t);
        node->data = NULL;
        node->syn = SYN_PLUS;
    } else  if ((*t)->lex == RIGHT_BRACE || (*t)->lex == END) {
        ++*t;
        free(node);
        node = NULL;
    } else {
        printf("syntax error(1) : not a plus nor end of expression.\n");
        exit(0);
    }
    return node;
}
struct AbstractSyntaxTree* parser(struct Token **t) //expr1
{
    struct AbstractSyntaxTree* node = malloc(sizeof(*node));
    if ((*t)->lex == IDENTIFIER) {
        node->syn = SYN_EXPRESSION;
        node->left = expr2(t);
        node->right = expr1_prime(t);
        node->data = NULL;
    } else {
        printf("syntax error!(0) : not a expression.\n");
        exit(0);
    }
    return node;
}

double variable[256] = {0};

double evaluate(struct AbstractSyntaxTree* node) {
    double val;
    if (node->syn == SYN_EXPRESSION || node->syn == SYN_PLUS) {
        val = evaluate(node->left);
        if (node->right != NULL) {
            if (node->right->syn == SYN_PLUS) {
                val += evaluate(node->right);
            }
        }
    } else if (node->syn == SYN_CALL) {
        if (strcmp(node->data, "cos") == 0) {
            val = cos(evaluate(node->left));
        } else if (strcmp(node->data, "sin") == 0) {
            val = sin(evaluate(node->left));
        } else if (strcmp(node->data, "tan") == 0) {
            val = tan(evaluate(node->left));
        }
    } else if (node->syn == SYN_IDENTIFIER) {
        val = variable[*(node->data)];
    }
    return val;
}

int main(void) {
    char input[256] = {0};
    const char *str = input;
    struct Token tokens[1024];
    int number_tokens = 0;
    int i;
    struct Token *p = tokens;
    struct AbstractSyntaxTree *root;
    double result;

    printf("you can use \"+\", \"cos(), sin(), tan()\", \"t\"(30degree) and |\"f\"(60degree)\n");
    printf(" input a expreesion :");
    scanf("%254s", input);

    while(str < &input[strlen(input)]) {
        struct Token token = lexer(&str);
        if (token.lex != WHITESPACE) {
            tokens[number_tokens++] = token;
        }
    }
    tokens[number_tokens++].lex = END;

    root = parser(&p);

    // t = 30 degree, f = 60 degree
    variable['t'] = 30.0 * 3.141592/180.0;
    variable['f'] = 60.0 * 3.141592/180.0;
    // calculate !!
    result = evaluate(root);

    printf("result : %f\n", result);

    // free all of node and data about root.
    return 0;
}