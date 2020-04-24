grammar ion;

root: NEWLINE root NEWLINE
    | head NEWLINE body NEWLINE
    | head elements NEWLINE
    | head NEWLINE
    | NEWLINE root
    | head NEWLINE body
    | head elements
    | head
    ;

body: TAB root
    | TAB elements
    ;

elements: elements IDENTIFIER
    | elements EQUAL
    | elements OTHER
    | IDENTIFIER
    | EQUAL
    | OTHER
    ;

head: IDENTIFIER attr COLON
    | IDENTIFIER empty COLON
    ;

empty: 
;

attr: attr_equal
    ;

attr_equal: IDENTIFIER EQUAL SQ other SQ
    | IDENTIFIER EQUAL DQ other DQ
    ;

other: other EQUAL
    | other COMMA
    | other COLON
    | other IDENTIFIER
    | other OTHER
    | EQUAL
    | COMMA
    | COLON
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