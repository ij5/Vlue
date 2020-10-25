import sys
from ast import *
from astor import code_gen
import time

############################
#####LEXER
############################

from ply import lex


class Lexer(object):
    reserved = {
        'if': 'IF',
        'else': 'ELSE',
        'function': 'FUNCTION',
        'repeat': 'REPEAT',
        'for': 'FOR',
        'while': 'WHILE',
        'in': 'IN',
        'use': 'USE',
        'try': 'TRY',
        'catch': 'CATCH',
        'global': 'GLOBAL',
        'class': 'CLASS',
        'do': 'DO',
        'end': 'END',
        'pass': 'PASS',
    }

    tokens = [
                 'IDENTIFIER',
                 'VAR',
                 'EQUAL',
                 'INT',
                 'FLOAT',
                 'STRING',
                 'LB',
                 'RB',
                 'COLON',
                 'SEMI',
                 'PLUS',
                 'MINUS',
                 'DIV',
                 'MUL',
                 'RSB',
                 'LSB',
                 'RMB',
                 'LMB',
                 'LBB',
                 'RBB',
                 'COMMA',
                 'DOT',
                 'NOTEQUAL',
                 'PYTHON',
                 'DL',
             ] + list(reserved.values())

    t_EQUAL = r'='
    t_DIV = r'\/'
    t_MUL = r'\*'
    t_PLUS = r'\+'
    t_MINUS = r'\-'
    t_LSB = r'\('
    t_RSB = r'\)'
    t_LMB = r'\{'
    t_RMB = r'\}'
    t_LB = r'\<'
    t_RB = r'\>'
    t_COLON = r'\:'
    t_SEMI = r'\;'
    t_COMMA = r'\,'
    t_DOT = r'\.'
    t_LBB = r'\['
    t_RBB = r'\]'
    t_NOTEQUAL = r'\!'
    t_DL = r'\$'

    t_ignore = ' '

    def t_TAB(self, t):
        r'\t'
        return t

    def t_VAR(self, t):
        r'var'
        return t

    def t_FLOAT(self, t):
        r'\d+\.\d+'
        t.value = float(t.value)
        return t

    def t_INT(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_CLASS(self, t):
        r'class'
        return t

    def t_STRING(self, t):
        r'("(?:\\"|.)*?"|\'(?:\\\'|.)*?\')'
        t.value = bytes(t.value, "utf-8").decode("unicode_escape")
        return t

    def t_IDENTIFIER(self, t):
        r'[a-zA-Z_]+[a-zA-Z_0-9]*'
        t.type = Lexer.reserved.get(t.value, t.type)
        return t

    def t_PYTHON(self, t):
        r'`[^`]+`'
        return t

    def t_NEWLINE(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)
        t.lexer.linepos = 0
        pass

    def t_error(self, t):
        print("error on token %s" % t.value)
        t.lexer.skip(1)

    def __init__(self):
        self.lexer = lex.lex(module=self)

    def test(self, data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            print(tok)


# data = '''
# if(a<b){
#     a = b;
# }else{
# a = b;
# }
# '''
#
# lexer.input(data)

# while True:
#     tok = lexer.token()
#     if not tok:
#         break
#     print(tok)
# print()


###################
#####PARSER
###################

from ply import yacc
import re
import os

code = "buf___ = 0\n"
variable = {}
state = []
f = []
debug = False

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MUL', 'DIV'),
    ('nonassoc', 'UMINUS')
)


def DecodeEscape(s):
    res = ''
    i = iter(s)
    for c in i:
        if c == '\\':
            c = next(i)
            if c == 'n':
                res += '\n'
            elif c == 'r':
                res += '\r'
            elif c == 't':
                res += '\t'
            elif c == '"':
                res += '"'
            elif c == "'":
                res += "'"
            elif c == 'x':
                try:
                    x = next(i)
                except StopIteration:
                    res += "\\x"
                    break
                try:
                    x += next(i)
                except StopIteration:
                    pass
                try:
                    x = int(x, 16)
                    res += chr(x)
                except ValueError:
                    res += '\\x' + x
            elif c == '\\':
                res += '\\'
            else:
                res += c
        else:
            res += c
    return res


class BaseNode():
    def __init__(self, VALUE=0, RETURN=0):
        self.VALUE = VALUE
        self.RETURN = RETURN


def flatten(listdata):
    return listdata[0]


def ex(data):
    return compile(data, '<string>', 'exec')


class AdvancedParser(object):
    tokens = Lexer.tokens
    reserved = Lexer.reserved
    precedence = precedence

    ##################### PROGRAM

    def p_program(self, t):
        '''
        program : root
        '''
        t[0] = BaseNode()
        t[0].VALUE = Module(body=t[1].VALUE)

    ##################### ROOT

    def p_root(self, t):
        '''
        root : root statement
            | statement
        '''
        t[0] = BaseNode()
        if len(t) == 3:
            t[1].VALUE.append(t[2].VALUE)
            t[0].VALUE = t[1].VALUE
        elif len(t) == 2:
            t[0].VALUE = [t[1].VALUE]

    ################### STATEMENT

    def p_statement(self, t):
        '''
        statement : if_statement
            | while_statement
            | variable_declaration SEMI
            | variable_value_change SEMI
            | function_declaration
            | PASS SEMI
            | use SEMI
            | python
            | class_declaration
            | empty
        '''
        t[0] = BaseNode()
        if t[1] == "<use>":
            t[0].VALUE = Not()
        else:
            t[0].VALUE = t[1].VALUE

    def p_statement_calculate(self, t):
        '''statement : expression SEMI'''
        t[0] = BaseNode()
        t[0].VALUE = Expr(t[1].VALUE)

    ################## EXPRESSION

    def p_expression(self, t):
        '''
        expression : calculate
            | string_calculate
            | compare_expression
            | function_call
            | list
            | variable_list
        '''
        t[0] = BaseNode()
        if isinstance(t[1].VALUE, int):
            t[0].VALUE = Num(n=t[1].VALUE)
        else:
            t[0].VALUE = t[1].VALUE

    ################### USE STATEMENT

    def p_use(self, t):
        '''use : USE IDENTIFIER'''
        t[0] = BaseNode()
        t[0].VALUE = None
        lib = t[1]
        libfile = lib + ".blib"
        realpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib", libfile)
        if os.path.isfile(realpath):
            f = open(realpath, 'r', encoding='UTF-8').read()
        else:
            print("There are no library named " + lib)

    def p_python(self, t):
        '''python : PYTHON'''
        t[0] = BaseNode()
        t[0].VALUE = None

    ################### VARIABLE DECLARATION

    def p_variable_declaration(self, t):
        '''
        variable_declaration : VAR IDENTIFIER EQUAL expression
            | VAR variable_list EQUAL expression
            | VAR IDENTIFIER
        '''
        t[0] = BaseNode()
        global variable
        if len(t) == 5:
            if isinstance(t[4].VALUE, Num):
                t[0].VALUE = Assign(targets=[Name(id=t[2].VALUE, ctx=Store())], value=t[4].VALUE)
                variable[t[2].VALUE] = t[4].VALUE.n
            else:
                t[0].VALUE = Assign(targets=[Name(id=t[2].VALUE, ctx=Store())], value=t[4].VALUE)
        else:
            t[0].VALUE = Assign(targets=[Name(id=t[2].VALUE, ctx=Store())], value=Num(0))
            variable[t[2].VALUE] = 0

    def p_variable_value_change(self, t):
        '''
        variable_value_change : IDENTIFIER EQUAL expression
            | variable_list EQUAL expression
        '''
        t[0] = BaseNode()
        if isinstance(t[3], Num):
            t[0].VALUE = Assign(targets=[Name(id=t[1], ctx=Store())], value=t[3].VALUE)
        elif isinstance(t[1], BaseNode):
            t[0].VALUE = Assign(targets=[Name(id=t[1].VALUE, ctx=Store())], value=t[3].VALUE)
        else:
            t[0].VALUE = Assign(targets=[Name(id=t[1], ctx=Store())], value=t[3].VALUE)

    ################### CLASS

    def p_class_declaration_1(self, t):
        '''class_declaration : CLASS IDENTIFIER LMB root RMB'''
        Module(body=[ClassDef(name='a', bases=[], keywords=[],
                              body=[Assign(targets=[Name(id='a', ctx=Store())], value=Num(n=5))], decorator_list=[])])
        t[0] = BaseNode()
        if (t[4].VALUE == [None]):
            t[4].VALUE.append(Pass())
        t[0].VALUE = ClassDef(name=t[2], bases=[], keywords=[], body=t[4].VALUE, decorator_list=[])

    def p_class_declaration_2(self, t):
        '''class_declaration : CLASS IDENTIFIER LSB class_decl_parameter RSB LMB root RMB'''
        t[0] = BaseNode()
        if (t[7].VALUE == [None]):
            t[7].VALUE.append(Pass())
        t[0].VALUE = ClassDef(name=t[2], bases=t[4].VALUE, keywords=[], body=t[7].VALUE, decorator_list=[])

    def p_class_decl_parameter(self, t):
        '''class_decl_parameter : class_decl_parameter COMMA IDENTIFIER
            | IDENTIFIER
        '''
        t[0] = BaseNode()
        if (len(t) == 2):
            t[0].VALUE = [Name(id=t[1], ctx=Load())]
        else:
            t[1].VALUE.append(Name(id=t[3], ctx=Load()))
            t[0].VALUE = t[1].VALUE

    ################### FUNCTION

    def p_function_call(self, t):
        '''function_call : IDENTIFIER LSB function_call_parameter RSB'''
        t[0] = BaseNode()
        t[0].VALUE = Call(func=Name(id=t[1], ctx=Load()), args=t[3].VALUE, keywords=[])
        Module(body=[Expr(value=Call(func=Name(id='print', ctx=Load()), args=[Num(n=0)], keywords=[]))])

    def p_function_call_parameter(self, t):
        '''
        function_call_parameter : function_call_parameter COMMA expression
            | expression
            | empty
        '''
        t[0] = BaseNode()
        if len(t) == 4:
            if isinstance(t[3].VALUE, str):
                t[1].VALUE.append(Name(t[3].VALUE))
            else:
                t[1].VALUE.append(t[3].VALUE)
            t[0].VALUE = t[1].VALUE
        elif len(t) == 2:
            if t[1].VALUE == None:
                t[0].VALUE = []
            else:
                if isinstance(t[1], str):
                    t[0].VALUE = [Name(t[1].VALUE)]
                else:
                    t[0].VALUE = [t[1].VALUE]

    def p_function_declaration(self, t):
        '''function_declaration : FUNCTION IDENTIFIER LSB function_parameter RSB LMB root RMB'''
        t[0] = BaseNode()
        if (t[7].VALUE == [None]):
            t[7].VALUE.append(Pass())
        t[0].VALUE = FunctionDef(name=t[2], args=arguments(
            args=t[4].VALUE,
            vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                                 body=t[7].VALUE, decorator_list=[], returns=None)

    def p_function_parameter(self, t):
        '''
        function_parameter : function_parameter COMMA IDENTIFIER
            | IDENTIFIER
            | empty
        '''
        t[0] = BaseNode()
        if (len(t) == 2):
            if (t[1].VALUE == None):
                t[0].VALUE = []
            else:
                t[0].VALUE = [arg(arg=t[1], annotation=None)]
        elif (len(t) == 4):
            t[1].VALUE.append(arg(arg=t[3], annotation=None))
            t[0].VALUE = t[1].VALUE

    ################### WHILE

    def p_while_statement(self, t):
        '''
        while_statement : WHILE LSB expression RSB LMB root RMB
        '''
        t[0] = BaseNode()
        if (t[6].VALUE == [None]):
            t[6].VALUE.append(Pass())
        t[0].VALUE = While(test=t[3].VALUE, body=t[6].VALUE, orelse=[])

    ################## IF

    def p_if_statement(self, t):
        '''
        if_statement : IF LSB expression RSB LMB root RMB
        '''
        t[0] = BaseNode()
        if (t[6].VALUE == [None]):
            t[6].VALUE.append(Pass())
        t[0].VALUE = If(test=t[3].VALUE, body=t[6].VALUE, orelse=[])

    def p_if_statement_elif(self, t):
        '''
        if_statement : if_statement ELSE IF LSB expression RSB LMB root RMB
        '''
        t[0] = BaseNode()
        if (t[8].VALUE == [None]):
            t[8].VALUE.append(Pass())
        t[1].VALUE.orelse.append(If(test=t[5].VALUE, body=t[8].VALUE, orelse=[]))
        t[0].VALUE = t[1].VALUE
        # else:
        #     t[1].orelse = [If(test=t[5], body=t[8])]
        #     t[0] = t[1]

    def p_if_statement_else(self, t):
        '''if_statement : if_statement ELSE LMB root RMB'''
        t[0] = BaseNode()
        if (t[4].VALUE == [None]):
            t[4].VALUE.append(Pass())
        try:
            t[1].VALUE.orelse[0].orelse.append(flatten(t[4]))
            t[0].VALUE = t[1].VALUE
        except(IndexError):
            t[1].VALUE.orelse.append(flatten(t[4]))
            t[0].VALUE = t[1].VALUE

    ################## COMPARE

    def p_compare_expression(self, t):
        '''
        compare_expression : compare_expression compare_operator calculate
            | calculate
        '''
        t[0] = BaseNode()
        if len(t) == 2:
            t[0].VALUE = t[1].VALUE
        elif len(t) == 4:
            if t[2].VALUE == '<':
                t[0].VALUE = Compare(left=t[1].VALUE, ops=[Lt()], comparators=[t[3].VALUE])
            elif t[2].VALUE == '>':
                t[0].VALUE = Compare(left=t[1].VALUE, ops=[Gt()], comparators=[t[3].VALUE])
            elif t[2].VALUE == '<=':
                t[0].VALUE = Compare(left=t[1].VALUE, ops=[LtE()], comparators=[t[3].VALUE])
            elif t[2].VALUE == '>=':
                t[0] = Compare(left=t[1].VALUE, ops=[GtE()], comparators=[t[3].VALUE])

    def p_compare_operator(self, t):
        '''
        compare_operator : LB
            | RB
            | LB EQUAL
            | RB EQUAL
            | EQUAL EQUAL
            | NOTEQUAL EQUAL
        '''
        t[0] = BaseNode()
        if len(t) == 2:
            t[0].VALUE = t[1]
        else:
            t[0].VALUE = t[1] + t[2]

    ################### LIST

    def p_list(self, t):
        '''list : LBB list_params RBB'''
        List(elts=[Num(n=1), Num(n=2), Num(n=3)], ctx=Load())
        t[0] = BaseNode()
        t[0].VALUE = List(elts=t[2].VALUE, ctx=Load())

    def p_list_params(self, t):
        '''
        list_params : list_params COMMA expression
            | expression
        '''
        t[0] = BaseNode()
        if len(t) == 2:
            t[0].VALUE = [t[1].VALUE]
        else:
            t[1].VALUE.append(t[3].VALUE)
            t[0] = t[1]

    def p_variable_list(self, t):
        '''variable_list : variable_list LBB expression RBB
        '''
        t[0] = BaseNode()
        t[0].VALUE = Subscript(value=t[1].VALUE, slice=Index(value=t[3].VALUE), ctx=Load())

    def p_variable_list_2(self, t):
        '''variable_list : IDENTIFIER LBB expression RBB'''
        t[0] = BaseNode()
        t[0].VALUE = Subscript(value=Name(id=t[1], ctx=Load()), slice=Index(value=t[3].VALUE, ctx=Load()))

    ################### CALCULATE

    def p_string_calculate(self, t):
        '''
        string_calculate : string_calculate stringoperator string_calculate
            | STRING
        '''
        t[0] = BaseNode()
        if len(t) == 2:
            t[0].VALUE = Str(s=t[1][1:-1])
        else:
            t[0].VALUE = BinOp(left=t[1].VALUE, op=Add(), right=t[3].VALUE)

    def p_string_calculate_sb(self, t):
        '''string_calculate : LSB string_calculate RSB'''
        t[0] = BaseNode()
        t[0].VALUE = t[2].VALUE

    def p_stringOperator(self, t):
        '''
        stringoperator : PLUS
        '''
        t[0] = BaseNode()
        t[0].VALUE = t[1]

    def p_calculate_binop(self, t):
        '''calculate : calculate PLUS calculate
                      | calculate MINUS calculate
                      | calculate MUL calculate
                      | calculate DIV calculate'''
        t[0] = BaseNode()
        if t[2] == '+': t[0].VALUE = BinOp(left=t[1].VALUE, op=Add(), right=t[3].VALUE)
        if t[2] == '-': t[0].VALUE = BinOp(left=t[1].VALUE, op=Sub(), right=t[3].VALUE)
        if t[2] == '*': t[0].VALUE = BinOp(left=t[1].VALUE, op=Mult(), right=t[3].VALUE)
        if t[2] == '/': t[0].VALUE = BinOp(left=t[1].VALUE, op=Div(), right=t[3].VALUE)

    def p_calculate_uminus(self, t):
        'calculate : MINUS calculate %prec UMINUS'
        t[0] = BaseNode()
        t[0].VALUE = -t[2]

    def p_calculate_group(self, t):
        'calculate : LSB calculate RSB'
        t[0] = BaseNode()
        t[0].VALUE = t[2]

    def p_calculate_number(self, t):
        '''calculate : INT
            | FLOAT'''
        t[0] = BaseNode()
        t[0].VALUE = Num(t[1])

    def p_calculate_identifier(self, t):
        'calculate : IDENTIFIER'
        t[0] = BaseNode()
        t[0].VALUE = Name(t[1])

    def p_calculate_global_identifier(self, t):
        'calculate : DL IDENTIFIER'
        t[0] = BaseNode()
        t[0].VALUE = Name(t[2])
        t[0].TYPE = "GLOBAL_IDENTIFIER"

    ############ EMPTY

    def p_empty(self, t):
        'empty : '
        t[0] = BaseNode()
        t[0].VALUE = None

    # 토큰 에러 처리
    def p_error(self, t):
        if (t):
            print("Error on token '" + str(t.value) + "', line " + str(t.lineno))
        else:
            print("Error on EOF")

    def __init__(self):
        self.lexer = Lexer()
        self.parser = yacc.yacc(module=self)


# def p_calculate(t):
#     '''
#     calculate : calculate baseoperator INT
#         | calculate baseoperator FLOAT
#     '''
#     if t[2]=='+':
#         t[0] = BinOp(left=t[1], op=Add(), right=Num( n=t[3] ))
#     elif t[2]=='-':
#         t[0] = BinOp(left=t[1], op=Sub(), right=Num(n=t[3]))
#     elif t[2]=='*':
#         t[0] = BinOp(left=t[1], op=Mult(), right=Num(n=t[3]))
#     elif t[2]=='/':
#         t[0] = BinOp(left=t[1], op=Div(), right=Num(n=t[3]))
#
# def p_calculate_identifier(t):
#     'calculate : calculate baseoperator IDENTIFIER'''
#     if t[2]=='+':
#         t[0] = BinOp(left=t[1], op=Add(), right=Name(id=t[3], ctx=Store()))
#     elif t[2]=='-':
#         t[0] = BinOp(left=t[1], op=Sub(), right=Name(id=t[3], ctx=Store()))
#     elif t[2]=='*':
#         t[0] = BinOp(left=t[1], op=Mult(), right=Name(id=t[3], ctx=Store()))
#     elif t[2]=='/':
#         t[0] = BinOp(left=t[1], op=Div(), right=Name(id=t[3], ctx=Store()))
#
# def p_calculate_type_int(t):
#     '''calculate : INT'''
#     t[0] = Num(n=t[1])
#
# def p_calculate_type_float(t):
#     '''calculate : FLOAT'''
#     t[0] = Num(n=t[1])
#
# def p_calculate_type_identifier(t):
#     '''
#     calculate : IDENTIFIER
#     '''
#     t[0] = Name(id=t[1], ctx=Store())
#
# def p_baseOperator(t):
#     '''
#     baseoperator : PLUS
#         | MINUS
#         | MUL
#         | DIV
#     '''
#     t[0] = t[1]


# 에러 처리
def error(s):
    print(s)
    exit(-1)
