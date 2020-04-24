grammar ion;

root: head NEWLINE body
    | head elements
    ;

head: IDENTIFIER COLON
    | IDENTIFIER attr_equal COLON
    ;

attr_equal: IDENTIFIER EQUAL SQ element_value SQ
    | IDENTIFIER EQUAL DQ element_value DQ
    ;

element_value: element_value COLON
    | element_value COMMA
    | element_value EQUAL
    | element_value IDENTIFIER
    | element_value OTHER
    | COLON
    | COMMA
    | EQUAL
    | IDENTIFIER
    | OTHER
    ;

DQ: '"';
SQ: '\'';
COLON: ':';
NEWLINE: '\n';
TAB: '\t';
COMMA: ',';
EQUAL: '=';
IDENTIFIER: [a-zA-Z]+;
OTHER: .;