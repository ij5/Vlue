#ifndef TOKEN
#define TOKEN

typedef enum {
    HTML = 1000,
    HEAD,
    BODY,

    EQUAL,
    LSB,
    LMB,
    RSB,
    RMB,
    EOF
}token;

#endif