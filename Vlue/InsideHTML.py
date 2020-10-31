from ast import *

############################
#####LEXER
############################

from ply import lex


class Lexer(object):
    reserved = {
        'if': 'IF',
        'else': 'ELSE',
        'fn': 'FUNCTION',
        'repeat': 'REPEAT',
        'for': 'FOR',
        'while': 'WHILE',
        'in': 'IN',
        'use': 'USE',
        'global': 'GLOBAL',
        'class': 'CLASS',
        'pass': 'PASS',
        'true': 'TRUE',
        'false': 'FALSE',
        'namespace': 'NAMESPACE',
        'this': 'THIS',
        'return': 'RETURN',
        'break': 'BREAK',
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

from astor import code_gen

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


"""
program : root

root : root statement
    | statement

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

statement : expression SEMI

expression : calculate
    | string_calculate
    | compare_expression
    | function_call
    | list
    | variable_list
    | dot

use : USE IDENTIFIER

python : PYTHON

variable_declaration : VAR IDENTIFIER EQUAL expression
    | VAR variable_list EQUAL expression
    | VAR IDENTIFIER

variable_value_change : IDENTIFIER EQUAL expression
    | variable_list EQUAL expression

dot : dot DOT dot

dot : calculate
    | function_call

class_declaration : CLASS IDENTIFIER LMB root RMB

class_declaration : CLASS IDENTIFIER LSB class_decl_parameter RSB LMB root RMB

class_decl_parameter : class_decl_parameter COMMA IDENTIFIER
            | IDENTIFIER

function_call : IDENTIFIER LSB function_call_parameter RSB

function_call_parameter : function_call_parameter COMMA expression
    | expression
    | emptyfunction_declaration : FUNCTION IDENTIFIER LSB function_parameter RSB LMB root RMB

function_parameter : function_parameter COMMA IDENTIFIER
    | IDENTIFIER
    | empty

while_statement : WHILE LSB expression RSB LMB root RMB

if_statement : IF LSB expression RSB LMB root RMB

if_statement : if_statement ELSE IF LSB expression RSB LMB root RMB

if_statement : if_statement ELSE LMB root RMB

compare_expression : compare_expression compare_operator calculate
    | calculate

compare_operator : LB
    | RB
    | LB EQUAL
    | RB EQUAL
    | EQUAL EQUAL
    | NOTEQUAL EQUAL

list : LBB list_params RBB 

list_params : list_params COMMA expression
            | expression

variable_list : variable_list LBB expression RBB

variable_list : IDENTIFIER LBB expression RBB

string_calculate : string_calculate stringoperator string_calculate
    | STRING

string_calculate : LSB string_calculate RSB
        stringoperator : PLUS

calculate : calculate PLUS calculate
      | calculate MINUS calculate
      | calculate MUL calculate
      | calculate DIV calculate

calculate : MINUS calculate %prec UMINUS

calculate : LSB calculate RSB

calculate : IDENTIFIER

calculate : FALSE

calculate : TRUE

calculate : DL IDENTIFIER

empty : 

"""


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


namespace = []


def flatten(listdata):
    return listdata[0]


def lookup(s, lookups):
    for pattern, value in lookups:
        if re.search(pattern, s):
            return value
    return None


def get_value(dic):
    try:
        return next(iter(dic.values()))
    except StopIteration:
        return None


class ElementaryParser(object):
    tokens = Lexer.tokens
    reserved = Lexer.reserved
    precedence = precedence
    debug = False

    ##################### PROGRAM

    def p_program(self, t):
        '''
        program : root
        '''
        t[0] = BaseNode()
        t[0].VALUE = Module(body=t[1].VALUE)
        t[0].TYPE = "PROGRAM"

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
        t[0].TYPE = "ROOT"

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
            | class_declaration
            | namespace SEMI
            | anon_function
            | anon_function SEMI
            | anon_function_vc
            | anon_function_vc SEMI
            | return SEMI
            | break SEMI
            | empty
        '''
        t[0] = BaseNode()
        if t[1] == "<use>":
            t[0].VALUE = Not()
        else:
            t[0].VALUE = t[1].VALUE
        t[0].TYPE = "STATEMENT"

    def p_statement_calculate(self, t):
        '''statement : expression SEMI'''
        t[0] = BaseNode()
        #t[0].VALUE = Expr(t[1].VALUE)
        t[0].TYPE = "STATEMENT"
        t[0].VALUE = Expr(Call(func=Name(id='print', ctx=Load()), args=[t[1].VALUE], keywords=[]))

    def p_statement_calculate_2(self, t):     #TODO: This statement will cause error.
        '''statement : expression'''
        t[0] = BaseNode()
        t[0].TYPE = 'STATEMENT'
        t[0].VALUE = Expr(Call(func=Name(id='print', ctx=Load()), args=[t[1].VALUE], keywords=[]))

        ################## EXPRESSION

    def p_expression(self, t):
        '''
        expression : calculate
        '''
        t[0] = BaseNode()
        if isinstance(t[1].VALUE, int):
            t[0].VALUE = Num(n=t[1].VALUE)
        else:
            t[0].VALUE = t[1].VALUE
        t[0].TYPE = t[1].TYPE

    ################### NAMESPACE STATEMENT

    def p_namespace(self, t):
        '''namespace : NAMESPACE IDENTIFIER'''
        t[0] = BaseNode()
        t[0].VALUE = None
        global namespace

    ################### USE STATEMENT

    def p_use(self, t):
        '''use : USE IDENTIFIER'''
        t[0] = BaseNode()
        t[0].VALUE = None
        lib = t[2]
        libfile = lib + ".py"
        realpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib", libfile)
        syslibfile = lib + ".sys.py"
        sysrealpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib", syslibfile)
        if os.path.isfile(realpath):
            f = open(realpath, 'r', encoding='UTF-8').read()
            ast = parse(f, "<string>", "exec")
            t[0].VALUE = ast
        elif os.path.isfile(sysrealpath):
            f = open(sysrealpath, 'r', encoding='UTF-8').read()
            exec(f)
        else:
            if (t[2] == "debug"):
                self.debug = True
            else:
                error("There are no library named " + lib)
        t[0].TYPE = "USE"

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
                if (isinstance(t[2], str)):
                    t[0].VALUE = Assign(targets=[Name(id=t[2], ctx=Store())], value=t[4].VALUE)
                else:
                    t[0].VALUE = Assign(targets=[Name(id=t[2].VALUE, ctx=Store())], value=t[4].VALUE)
            else:
                if (isinstance(t[2], str)):
                    t[0].VALUE = Assign(targets=[Name(id=t[2], ctx=Store())], value=t[4].VALUE)
                else:
                    t[0].VALUE = Assign(targets=[Name(id=t[2].VALUE, ctx=Store())], value=t[4].VALUE)
        else:
            t[0].VALUE = Assign(targets=[Name(id=t[2].VALUE, ctx=Store())], value=Num(0))
            variable[t[2].VALUE] = 0
        t[0].TYPE = "VARIABLE_DECLARATION"

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
        t[0].TYPE = "VARIABLE_VALUE_CHANGE"

    ################### DOT

    def p_inside(self, t):
        '''inside : inside DOT inside'''
        t[0] = BaseNode()
        t[0].VALUE = Attribute(value=t[1].VALUE, attr=t[3].VALUE, ctx=Load())
        t[0].TYPE = "INSIDE"

    def p_inside_attr(self, t):
        '''
        inside : IDENTIFIER
        '''
        t[0] = BaseNode()
        t[0].VALUE = Name(id=t[1], ctx=Store())
        t[0].TYPE = "IDENTIFIER"

    def p_inside_attr_2(self, t):
        '''inside : function_call'''
        t[0] = BaseNode()
        t[0].VALUE = t[1].VALUE
        t[0].TYPE = t[1].TYPE

    #
    # def p_dot(self, t):             #TODO DOT
    #     '''
    #     dot : dot DOT dot_attr
    #         | dot_attr
    #     '''
    #     t[0] = BaseNode()
    #     if(len(t)==4):
    #         if(t[1].TYPE == "IDENTIFIER"):
    #             if(t[3].TYPE=="IDENTIFIER"):
    #                 t[0].VALUE = Attribute(value=t[1].VALUE, attr=t[3].VALUE, ctx=Load())
    #             elif(t[3].TYPE=="FUNCTION_CALL"):
    #                 t[0].VALUE = Attribute(value=t[1].VALUE, attr=t[3].VALUE, ctx=Load())
    #             t[0].TYPE = "DOT"
    #         elif(t[1].TYPE=="FUNCTION_CALL"):
    #             if(t[3].TYPE=="IDENTIFIER"):
    #                 t[0].VALUE = Attribute(value=t[1].VALUE, attr=t[3].VALUE, ctx=Load())
    #             elif(t[3].TYPE=="FUNCTION_CALL"):
    #                 t[0].VALUE = Attribute(value=t[1].VALUE, attr=t[3].VALUE, ctx=Load())
    #             t[0].TYPE = "DOT"
    #         elif(t[1].TYPE=="DOT"):
    #             t[0].VALUE = Attribute(value=t[1].VALUE, attr=t[3].VALUE, ctx=Load())
    #             t[0].TYPE = "DOT"
    #         else:
    #             error("Syntax Error on line "+str(t.lineno(1)))
    #     else:
    #         t[0].VALUE = t[1].VALUE
    #         t[0].TYPE = t[1].TYPE
    #
    # def p_dot_attr(self, t):
    #     '''
    #     dot_attr : calculate
    #     '''
    #     t[0] = BaseNode()
    #     if(t[1].TYPE=="IDENTIFIER"):
    #         t[0].VALUE = t[1].VALUE
    #         t[0].TYPE = "IDENTIFIER"
    #     elif(t[1].TYPE=="FUNCTION_CALL"):
    #         t[0].VALUE = t[1].VALUE
    #         t[0].TYPE = "FUNCTION_CALL"
    #     else:
    #         error("syntax Error on line "+str(t.lineno(1)))

    ################### BREAK

    def p_break(self, t):
        '''break : BREAK'''
        t[0] = BaseNode()
        t[0].VALUE = Break()
        t[0].TYPE = "BREAK"

    ################### RETURN

    def p_return(self, t):
        '''return : RETURN expression'''
        t[0] = BaseNode()
        t[0].TYPE = "RETURN"
        t[0].VALUE = Return(value=t[2].VALUE)

    ################### CLASS

    def p_class_declaration_1(self, t):
        '''class_declaration : CLASS IDENTIFIER LMB root RMB'''
        Module(body=[ClassDef(name='a', bases=[], keywords=[],
                              body=[Assign(targets=[Name(id='a', ctx=Store())], value=Num(n=5))], decorator_list=[])])
        t[0] = BaseNode()
        if (t[4].VALUE == [None]):
            t[4].VALUE.append(Pass())
        t[0].VALUE = ClassDef(name=t[2], bases=[], keywords=[], body=t[4].VALUE, decorator_list=[])
        t[0].TYPE = "CLASS_DECLARATION"

    def p_class_declaration_2(self, t):
        '''class_declaration : CLASS IDENTIFIER LSB class_decl_parameter RSB LMB root RMB'''
        t[0] = BaseNode()
        if (t[7].VALUE == [None]):
            t[7].VALUE.append(Pass())
        t[0].VALUE = ClassDef(name=t[2], bases=t[4].VALUE, keywords=[], body=t[7].VALUE, decorator_list=[])
        t[0].TYPE = "CLASS_DECLARATION"

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
        t[0].TYPE = "CLASS_DECL_PARAMETER"

    ################### FUNCTION

    def p_anon_function(self, t):
        '''anon_function : VAR IDENTIFIER EQUAL FUNCTION LSB function_parameter RSB LMB root RMB'''
        t[0] = BaseNode()
        if (t[9].VALUE == [None]):
            t[9].VALUE.append(Pass())
        t[0].VALUE = FunctionDef(name=t[2], args=arguments(
            args=t[6].VALUE,
            vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                                 body=t[9].VALUE, decorator_list=[], returns=None)
        t[0].TYPE = "ANON_FUNCTION"

    def p_anon_function_vc(self, t):
        '''anon_function_vc : IDENTIFIER EQUAL FUNCTION LSB function_parameter RSB LMB root RMB'''
        t[0] = BaseNode()
        if (t[8].VALUE == [None]):
            t[8].VALUE.append(Pass())
        t[0].VALUE = FunctionDef(name=t[1], args=arguments(
            args=t[5].VALUE,
            vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                                 body=t[8].VALUE, decorator_list=[], returns=None)
        t[0].TYPE = "ANON_FUNCTION_VC"

    def p_function_call(self, t):
        '''function_call : IDENTIFIER LSB function_call_parameter RSB'''
        t[0] = BaseNode()
        t[0].VALUE = Call(func=Name(id=t[1], ctx=Load()), args=t[3].VALUE, keywords=[])
        Module(body=[Expr(value=Call(func=Name(id='print', ctx=Load()), args=[Num(n=0)], keywords=[]))])
        t[0].TYPE = "FUNCTION_CALL"

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
        t[0].TYPE = "FUNCTION_CALL_PARAMETER"

    def p_function_declaration(self, t):
        '''function_declaration : FUNCTION IDENTIFIER LSB function_parameter RSB LMB root RMB'''
        t[0] = BaseNode()
        if (t[7].VALUE == [None]):
            t[7].VALUE.append(Pass())
        t[0].VALUE = FunctionDef(name=t[2], args=arguments(
            args=t[4].VALUE,
            vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                                 body=t[7].VALUE, decorator_list=[], returns=None)
        t[0].TYPE = "FUNCTION_DECLARATION"

    def p_function_parameter(self, t):
        '''
        function_parameter : function_parameter COMMA IDENTIFIER
            | IDENTIFIER
            | empty
        '''
        t[0] = BaseNode()
        if (len(t) == 2):
            if (isinstance(t[1], str)):
                t[0].VALUE = [arg(arg=t[1], annotation=None)]
            else:
                t[0].VALUE = []
        elif (len(t) == 4):
            t[1].VALUE.append(arg(arg=t[3], annotation=None))
            t[0].VALUE = t[1].VALUE
        t[0].TYPE = "FUNCTION_PARAMETER"

        ################### WHILE

    def p_while_statement(self, t):
        '''
        while_statement : WHILE LSB expression RSB LMB root RMB
        '''
        t[0] = BaseNode()
        if (t[6].VALUE == [None]):
            t[6].VALUE.append(Pass())
        t[0].VALUE = While(test=t[3].VALUE, body=t[6].VALUE, orelse=[])
        t[0].TYPE = "WHILE_STATEMENT"

        ################## IF

    def p_if_statement(self, t):
        '''
        if_statement : IF LSB expression RSB LMB root RMB
        '''
        t[0] = BaseNode()
        if (t[6].VALUE == [None]):
            t[6].VALUE.append(Pass())
        t[0].VALUE = If(test=t[3].VALUE, body=t[6].VALUE, orelse=[])
        t[0].TYPE = "IF_STATEMENT"

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
        t[0].TYPE = "IF_STATEMENT"

    def p_if_statement_else(self, t):
        '''if_statement : if_statement ELSE LMB root RMB'''
        t[0] = BaseNode()
        if (t[4].VALUE == [None]):
            t[4].VALUE.append(Pass())
        try:
            t[1].VALUE.orelse[0].orelse.append(flatten(t[4].VALUE))
            t[0].VALUE = t[1].VALUE
        except(IndexError):
            t[1].VALUE.orelse.append(flatten(t[4].VALUE))
            t[0].VALUE = t[1].VALUE
        t[0].TYPE = "IF_STATEMENT"

        ################## COMPARE TODO: OR AND

    def p_compare_expression(self, t):
        '''
        compare_expression : expression compare_operator expression
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
                t[0].VALUE = Compare(left=t[1].VALUE, ops=[GtE()], comparators=[t[3].VALUE])
            elif t[2].VALUE == "==":
                t[0].VALUE = Compare(left=t[1].VALUE, ops=[Eq()], comparators=[t[3].VALUE])
            elif t[2].VALUE == "!=":
                t[0].VALUE = Compare(left=t[1].VALUE, ops=[NotEq()], comparators=[t[3].VALUE])
        t[0].TYPE = "COMPARE_EXPRESSION"

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
        t[0].TYPE = "COMPARE_OPERATOR"

        ################### LIST

    def p_list(self, t):
        '''list : LBB list_params RBB'''
        List(elts=[Num(n=1), Num(n=2), Num(n=3)], ctx=Load())
        t[0] = BaseNode()
        t[0].VALUE = List(elts=t[2].VALUE, ctx=Load())
        t[0].TYPE = "LIST"

    def p_list_params(self, t):
        '''
        list_params : list_params COMMA expression
            | expression
            | empty
        '''
        t[0] = BaseNode()
        if len(t) == 2:
            if (t[1] != None):
                t[0].VALUE = [t[1].VALUE]
            else:
                t[0].VALUE = [t[1].VALUE]
        else:
            t[1].VALUE.append(t[3].VALUE)
            t[0] = t[1]

        t[0].TYPE = "LIST_PARAMS"

    def p_variable_list(self, t):
        '''variable_list : variable_list LBB expression RBB
        '''
        t[0] = BaseNode()
        t[0].VALUE = Subscript(value=t[1].VALUE, slice=Index(value=t[3].VALUE), ctx=Load())
        t[0].TYPE = "VARIABLE_LIST"

    def p_variable_list_2(self, t):
        '''variable_list : IDENTIFIER LBB expression RBB'''
        t[0] = BaseNode()
        t[0].VALUE = Subscript(value=Name(id=t[1], ctx=Load()), slice=Index(value=t[3].VALUE, ctx=Load()))
        t[0].TYPE = "VARIABLE_LIST"

        ################### CALCULATE

    #
    # def p_string_calculate(self, t):
    #     '''
    #     string_calculate : string_calculate stringoperator string_calculate
    #         | STRING
    #     '''
    #     t[0] = BaseNode()
    #     if len(t)==2:
    #         t[0].VALUE = Str(s=t[1][1:-1])
    #     else:
    #         t[0].VALUE = BinOp(left=t[1].VALUE, op=Add(), right=t[3].VALUE)
    #     t[0].TYPE = "STRING"
    #
    # def p_string_calculate_sb(self, t):
    #     '''string_calculate : LSB string_calculate RSB'''
    #     t[0] = BaseNode()
    #     t[0].VALUE = t[2].VALUE
    #     t[0].TYPE = "STRING"
    #
    # def p_stringOperator(self, t):
    #     '''
    #     stringoperator : PLUS
    #     '''
    #     t[0] = BaseNode()
    #     t[0].VALUE = t[1]
    #     t[0].TYPE = " PLUS"

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
        t[0].TYPE = "BINOP"

    def p_calculate_function_call(self, t):
        '''calculate : function_call'''
        t[0] = BaseNode()
        t[0].VALUE = t[1].VALUE
        t[0].TYPE = t[1].TYPE

    def p_calculate_uminus(self, t):
        'calculate : MINUS calculate %prec UMINUS'
        t[0] = BaseNode()
        t[0].VALUE = -t[2]
        t[0].TYPE = "MINUS"

    def p_calculate_group(self, t):
        'calculate : LSB calculate RSB'
        t[0] = BaseNode()
        t[0].VALUE = t[2].VALUE
        t[0].TYPE = "GROUP"

    def p_calculate_number(self, t):
        '''calculate : INT
            | FLOAT'''
        t[0] = BaseNode()
        t[0].VALUE = Num(t[1])
        t[0].TYPE = "NUMBER"

    def p_calculate_identifier(self, t):
        'calculate : IDENTIFIER'
        t[0] = BaseNode()
        t[0].VALUE = Name(t[1])
        t[0].TYPE = "IDENTIFIER"
        t[0].RAW = t[1]

    def p_calculate_string(self, t):
        'calculate : STRING'
        t[0] = BaseNode()
        t[0].VALUE = Str(s=t[1][1:-1])
        t[0].TYPE = "STRING"

    def p_calculate_boolean_false(self, t):
        'calculate : FALSE'
        t[0] = BaseNode()
        t[0].VALUE = NameConstant(value=False)
        t[0].TYPE = "BOOLEAN_FALSE"

    def p_calculate_boolean_true(self, t):
        'calculate : TRUE'
        t[0] = BaseNode()
        t[0].VALUE = NameConstant(value=True)
        t[0].TYPE = "BOOLEAN_TRUE"
        print("true")

    def p_calculate_compare_expression(self, t):
        '''calculate : compare_expression'''
        t[0] = BaseNode()
        t[0].VALUE = t[1].VALUE
        t[0].TYPE = t[1].TYPE

    def p_calculate_list(self, t):
        '''calculate : list'''
        t[0] = BaseNode()
        t[0].VALUE = t[1].VALUE
        t[0].TYPE = t[1].TYPE


    def p_calculate_variable_list(self, t):
        '''calculate : variable_list'''
        t[0] = BaseNode()
        t[0].VALUE = t[1].VALUE
        t[0].TYPE = t[1].TYPE

    # def p_calculate_dot(self, t):
    #     '''calculate : dot'''
    #     t[0] = BaseNode()
    #     t[0].VALUE = t[1].VALUE
    #     t[0].TYPE = t[1].TYPE

    def p_calculate_inside(self, t):
        '''calculate : inside'''
        t[0] = BaseNode()
        t[0].VALUE = t[1].VALUE
        t[0].TYPE = t[1].TYPE



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
        t[0].TYPE = "EMPTY"

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


def error(s):
    print(s)
    exit(-1)
