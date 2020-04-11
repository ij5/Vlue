#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

enum Lexicon {WHITESPACE, IDENTIFIER, PLUS, LEFT_BRACE, RIGHT_BRACE};

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

int main(void) {
    const char *input = "cos(t) + sin(f)";
    const char *str = input;
    struct Token tokens[1024];
    int number_tokens = 0;
    int i;

    while(str < &input[strlen(input)]) {
        struct Token token = lexer(&str);
        if (token.lex != WHITESPACE) {
            tokens[number_tokens++] = token;
        }
    }

    // print all tockens for test
    for(i=0; i<number_tokens; ++i) {
        const char* message [] = {"whitespace", "identifier", "+", "(", ")"};
        printf("%s\n", message[tokens[i].lex]);
    }

    return 0;
}