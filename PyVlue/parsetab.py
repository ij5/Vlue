
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'programleftPLUSMINUSleftMULDIVnonassocUMINUSCATCH CLASS COLON COMMA DIV DO DOT ELSE END EQUAL FLOAT FOR FUNCTION GLOBAL IDENTIFIER IF IN INT LB LBB LIST LMB LSB MINUS MUL NOTEQUAL PASS PLUS RB RBB REPEAT RMB RSB SEMI STRING TRY USE VAR WHILE\n    program : root\n    \n    root : root statement\n        | statement\n    \n    statement : if_statement\n        | while_statement\n        | variable_declaration SEMI\n        | variable_value_change SEMI\n        | function_declaration\n        | PASS SEMI\n        | use SEMI\n        | empty\n    statement : expression SEMI\n    expression : calculate\n        | string_calculate\n        | compare_expression\n        | function_call\n    use : USE IDENTIFIER\n    variable_declaration : VAR IDENTIFIER EQUAL expression\n        | VAR IDENTIFIER\n    \n    variable_value_change : IDENTIFIER EQUAL expression\n    function_call : IDENTIFIER LSB function_call_parameter RSB\n    function_call_parameter : function_call_parameter COMMA calculate\n        | calculate\n        | empty\n    function_declaration : FUNCTION IDENTIFIER LSB function_parameter RSB LMB root RMB\n    function_parameter : function_parameter COMMA IDENTIFIER\n        | IDENTIFIER\n        | empty\n    \n    while_statement : WHILE LSB expression RSB LMB root RMB\n    \n    if_statement : IF LSB expression RSB LMB root RMB\n    \n    if_statement : if_statement ELSE IF LSB expression RSB LMB root RMB\n    if_statement : if_statement ELSE LMB root RMB\n    compare_expression : compare_expression compare_operator calculate\n        | calculate\n    \n    compare_operator : LB\n        | RB\n        | LB EQUAL\n        | RB EQUAL\n        | EQUAL EQUAL\n        | NOTEQUAL EQUAL\n    \n    string_calculate : string_calculate stringoperator STRING\n        | STRING\n    \n    stringoperator : PLUS\n    calculate : calculate PLUS calculate\n                  | calculate MINUS calculate\n                  | calculate MUL calculate\n                  | calculate DIV calculatecalculate : MINUS calculate %prec UMINUScalculate : LSB calculate RSBcalculate : INTcalculate : IDENTIFIERempty : '
    
_lr_action_items = {'PASS':([0,2,3,4,5,8,11,27,29,30,31,32,33,56,78,88,89,90,95,96,97,99,100,101,102,103,104,105,],[9,9,-3,-4,-5,-8,-11,-2,-6,-7,-9,-10,-12,9,9,-32,9,9,9,9,9,9,-30,-29,9,9,-25,-31,]),'IF':([0,2,3,4,5,8,11,27,28,29,30,31,32,33,56,78,88,89,90,95,96,97,99,100,101,102,103,104,105,],[13,13,-3,-4,-5,-8,-11,-2,55,-6,-7,-9,-10,-12,13,13,-32,13,13,13,13,13,13,-30,-29,13,13,-25,-31,]),'WHILE':([0,2,3,4,5,8,11,27,29,30,31,32,33,56,78,88,89,90,95,96,97,99,100,101,102,103,104,105,],[15,15,-3,-4,-5,-8,-11,-2,-6,-7,-9,-10,-12,15,15,-32,15,15,15,15,15,15,-30,-29,15,15,-25,-31,]),'VAR':([0,2,3,4,5,8,11,27,29,30,31,32,33,56,78,88,89,90,95,96,97,99,100,101,102,103,104,105,],[16,16,-3,-4,-5,-8,-11,-2,-6,-7,-9,-10,-12,16,16,-32,16,16,16,16,16,16,-30,-29,16,16,-25,-31,]),'IDENTIFIER':([0,2,3,4,5,8,11,14,16,18,19,24,27,29,30,31,32,33,34,37,39,40,43,44,45,46,49,50,51,56,61,66,73,74,75,76,77,78,83,88,89,90,93,95,96,97,99,100,101,102,103,104,105,],[17,17,-3,-4,-5,-8,-11,36,38,41,42,36,-2,-6,-7,-9,-10,-12,58,58,58,36,36,36,36,36,36,-35,-36,17,58,84,-37,-38,-39,-40,58,17,36,-32,17,17,98,17,17,17,17,-30,-29,17,17,-25,-31,]),'FUNCTION':([0,2,3,4,5,8,11,27,29,30,31,32,33,56,78,88,89,90,95,96,97,99,100,101,102,103,104,105,],[18,18,-3,-4,-5,-8,-11,-2,-6,-7,-9,-10,-12,18,18,-32,18,18,18,18,18,18,-30,-29,18,18,-25,-31,]),'USE':([0,2,3,4,5,8,11,27,29,30,31,32,33,56,78,88,89,90,95,96,97,99,100,101,102,103,104,105,],[19,19,-3,-4,-5,-8,-11,-2,-6,-7,-9,-10,-12,19,19,-32,19,19,19,19,19,19,-30,-29,19,19,-25,-31,]),'MINUS':([0,2,3,4,5,8,11,14,17,20,24,25,27,29,30,31,32,33,34,35,36,37,39,40,43,44,45,46,49,50,51,54,56,58,59,61,64,67,68,69,70,72,73,74,75,76,77,78,83,88,89,90,91,95,96,97,99,100,101,102,103,104,105,],[24,24,-3,-4,-5,-8,-11,24,-51,44,24,-50,-2,-6,-7,-9,-10,-12,24,44,-51,24,24,24,24,24,24,24,24,-35,-36,-48,24,-51,-49,24,44,-44,-45,-46,-47,44,-37,-38,-39,-40,24,24,24,-32,24,24,44,24,24,24,24,-30,-29,24,24,-25,-31,]),'LSB':([0,2,3,4,5,8,11,13,14,15,17,24,27,29,30,31,32,33,34,37,39,40,41,43,44,45,46,49,50,51,55,56,58,61,73,74,75,76,77,78,83,88,89,90,95,96,97,99,100,101,102,103,104,105,],[14,14,-3,-4,-5,-8,-11,34,14,37,40,14,-2,-6,-7,-9,-10,-12,14,14,14,14,66,14,14,14,14,14,-35,-36,77,14,40,14,-37,-38,-39,-40,14,14,14,-32,14,14,14,14,14,14,-30,-29,14,14,-25,-31,]),'INT':([0,2,3,4,5,8,11,14,24,27,29,30,31,32,33,34,37,39,40,43,44,45,46,49,50,51,56,61,73,74,75,76,77,78,83,88,89,90,95,96,97,99,100,101,102,103,104,105,],[25,25,-3,-4,-5,-8,-11,25,25,-2,-6,-7,-9,-10,-12,25,25,25,25,25,25,25,25,25,-35,-36,25,25,-37,-38,-39,-40,25,25,25,-32,25,25,25,25,25,25,-30,-29,25,25,-25,-31,]),'STRING':([0,2,3,4,5,8,11,27,29,30,31,32,33,34,37,39,47,48,56,61,77,78,88,89,90,95,96,97,99,100,101,102,103,104,105,],[26,26,-3,-4,-5,-8,-11,-2,-6,-7,-9,-10,-12,26,26,26,71,-43,26,26,26,26,-32,26,26,26,26,26,26,-30,-29,26,26,-25,-31,]),'$end':([0,1,2,3,4,5,8,11,27,29,30,31,32,33,88,100,101,104,105,],[-52,0,-1,-3,-4,-5,-8,-11,-2,-6,-7,-9,-10,-12,-32,-30,-29,-25,-31,]),'RMB':([3,4,5,8,11,27,29,30,31,32,33,56,78,88,89,90,95,96,97,99,100,101,102,103,104,105,],[-3,-4,-5,-8,-11,-2,-6,-7,-9,-10,-12,-52,88,-32,-52,-52,100,101,-52,-52,-30,-29,104,105,-25,-31,]),'ELSE':([4,88,100,105,],[28,-32,-30,-31,]),'SEMI':([6,7,9,10,12,17,20,21,22,23,25,26,36,38,42,54,58,59,62,67,68,69,70,71,72,81,82,],[29,30,31,32,33,-51,-13,-14,-15,-16,-50,-42,-51,-19,-17,-48,-51,-49,-20,-44,-45,-46,-47,-41,-33,-18,-21,]),'EQUAL':([17,20,22,25,36,38,50,51,52,53,54,58,59,67,68,69,70,72,],[39,-34,52,-50,-51,61,73,74,75,76,-48,-51,-49,-44,-45,-46,-47,-33,]),'PLUS':([17,20,21,25,26,35,36,54,58,59,64,67,68,69,70,71,72,91,],[-51,43,48,-50,-42,43,-51,-48,-51,-49,43,-44,-45,-46,-47,-41,43,43,]),'MUL':([17,20,25,35,36,54,58,59,64,67,68,69,70,72,91,],[-51,45,-50,45,-51,-48,-51,-49,45,45,45,-46,-47,45,45,]),'DIV':([17,20,25,35,36,54,58,59,64,67,68,69,70,72,91,],[-51,46,-50,46,-51,-48,-51,-49,46,46,46,-46,-47,46,46,]),'LB':([17,20,22,25,36,54,58,59,67,68,69,70,72,],[-51,-34,50,-50,-51,-48,-51,-49,-44,-45,-46,-47,-33,]),'RB':([17,20,22,25,36,54,58,59,67,68,69,70,72,],[-51,-34,51,-50,-51,-48,-51,-49,-44,-45,-46,-47,-33,]),'NOTEQUAL':([17,20,22,25,36,54,58,59,67,68,69,70,72,],[-51,-34,53,-50,-51,-48,-51,-49,-44,-45,-46,-47,-33,]),'RSB':([20,21,22,23,25,26,35,36,40,54,57,58,59,60,63,64,65,66,67,68,69,70,71,72,82,84,85,86,87,91,98,],[-13,-14,-15,-16,-50,-42,59,-51,-52,-48,79,-51,-49,80,82,-23,-24,-52,-44,-45,-46,-47,-41,-33,-21,-27,92,-28,94,-22,-26,]),'COMMA':([25,36,40,54,59,63,64,65,66,67,68,69,70,84,85,86,91,98,],[-50,-51,-52,-48,-49,83,-23,-24,-52,-44,-45,-46,-47,-27,93,-28,-22,-26,]),'LMB':([28,79,80,92,94,],[56,89,90,97,99,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'root':([0,56,89,90,97,99,],[2,78,95,96,102,103,]),'statement':([0,2,56,78,89,90,95,96,97,99,102,103,],[3,27,3,27,3,3,27,27,3,3,27,27,]),'if_statement':([0,2,56,78,89,90,95,96,97,99,102,103,],[4,4,4,4,4,4,4,4,4,4,4,4,]),'while_statement':([0,2,56,78,89,90,95,96,97,99,102,103,],[5,5,5,5,5,5,5,5,5,5,5,5,]),'variable_declaration':([0,2,56,78,89,90,95,96,97,99,102,103,],[6,6,6,6,6,6,6,6,6,6,6,6,]),'variable_value_change':([0,2,56,78,89,90,95,96,97,99,102,103,],[7,7,7,7,7,7,7,7,7,7,7,7,]),'function_declaration':([0,2,56,78,89,90,95,96,97,99,102,103,],[8,8,8,8,8,8,8,8,8,8,8,8,]),'use':([0,2,56,78,89,90,95,96,97,99,102,103,],[10,10,10,10,10,10,10,10,10,10,10,10,]),'empty':([0,2,40,56,66,78,89,90,95,96,97,99,102,103,],[11,11,65,11,86,11,11,11,11,11,11,11,11,11,]),'expression':([0,2,34,37,39,56,61,77,78,89,90,95,96,97,99,102,103,],[12,12,57,60,62,12,81,87,12,12,12,12,12,12,12,12,12,]),'calculate':([0,2,14,24,34,37,39,40,43,44,45,46,49,56,61,77,78,83,89,90,95,96,97,99,102,103,],[20,20,35,54,20,20,20,64,67,68,69,70,72,20,20,20,20,91,20,20,20,20,20,20,20,20,]),'string_calculate':([0,2,34,37,39,56,61,77,78,89,90,95,96,97,99,102,103,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'compare_expression':([0,2,34,37,39,56,61,77,78,89,90,95,96,97,99,102,103,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'function_call':([0,2,34,37,39,56,61,77,78,89,90,95,96,97,99,102,103,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'stringoperator':([21,],[47,]),'compare_operator':([22,],[49,]),'function_call_parameter':([40,],[63,]),'function_parameter':([66,],[85,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> root','program',1,'p_program','main.py',1142),
  ('root -> root statement','root',2,'p_root','main.py',1150),
  ('root -> statement','root',1,'p_root','main.py',1151),
  ('statement -> if_statement','statement',1,'p_statement','main.py',1163),
  ('statement -> while_statement','statement',1,'p_statement','main.py',1164),
  ('statement -> variable_declaration SEMI','statement',2,'p_statement','main.py',1165),
  ('statement -> variable_value_change SEMI','statement',2,'p_statement','main.py',1166),
  ('statement -> function_declaration','statement',1,'p_statement','main.py',1167),
  ('statement -> PASS SEMI','statement',2,'p_statement','main.py',1168),
  ('statement -> use SEMI','statement',2,'p_statement','main.py',1169),
  ('statement -> empty','statement',1,'p_statement','main.py',1170),
  ('statement -> expression SEMI','statement',2,'p_statement_calculate','main.py',1178),
  ('expression -> calculate','expression',1,'p_expression','main.py',1185),
  ('expression -> string_calculate','expression',1,'p_expression','main.py',1186),
  ('expression -> compare_expression','expression',1,'p_expression','main.py',1187),
  ('expression -> function_call','expression',1,'p_expression','main.py',1188),
  ('use -> USE IDENTIFIER','use',2,'p_use','main.py',1198),
  ('variable_declaration -> VAR IDENTIFIER EQUAL expression','variable_declaration',4,'p_variable_declaration','main.py',1205),
  ('variable_declaration -> VAR IDENTIFIER','variable_declaration',2,'p_variable_declaration','main.py',1206),
  ('variable_value_change -> IDENTIFIER EQUAL expression','variable_value_change',3,'p_variable_value_change','main.py',1221),
  ('function_call -> IDENTIFIER LSB function_call_parameter RSB','function_call',4,'p_function_call','main.py',1233),
  ('function_call_parameter -> function_call_parameter COMMA calculate','function_call_parameter',3,'p_function_call_parameter','main.py',1239),
  ('function_call_parameter -> calculate','function_call_parameter',1,'p_function_call_parameter','main.py',1240),
  ('function_call_parameter -> empty','function_call_parameter',1,'p_function_call_parameter','main.py',1241),
  ('function_declaration -> FUNCTION IDENTIFIER LSB function_parameter RSB LMB root RMB','function_declaration',8,'p_function_declaration','main.py',1259),
  ('function_parameter -> function_parameter COMMA IDENTIFIER','function_parameter',3,'p_function_parameter','main.py',1264),
  ('function_parameter -> IDENTIFIER','function_parameter',1,'p_function_parameter','main.py',1265),
  ('function_parameter -> empty','function_parameter',1,'p_function_parameter','main.py',1266),
  ('while_statement -> WHILE LSB expression RSB LMB root RMB','while_statement',7,'p_while_statement','main.py',1284),
  ('if_statement -> IF LSB expression RSB LMB root RMB','if_statement',7,'p_if_statement','main.py',1292),
  ('if_statement -> if_statement ELSE IF LSB expression RSB LMB root RMB','if_statement',9,'p_if_statement_elif','main.py',1298),
  ('if_statement -> if_statement ELSE LMB root RMB','if_statement',5,'p_if_statement_else','main.py',1307),
  ('compare_expression -> compare_expression compare_operator calculate','compare_expression',3,'p_compare_expression','main.py',1319),
  ('compare_expression -> calculate','compare_expression',1,'p_compare_expression','main.py',1320),
  ('compare_operator -> LB','compare_operator',1,'p_compare_operator','main.py',1336),
  ('compare_operator -> RB','compare_operator',1,'p_compare_operator','main.py',1337),
  ('compare_operator -> LB EQUAL','compare_operator',2,'p_compare_operator','main.py',1338),
  ('compare_operator -> RB EQUAL','compare_operator',2,'p_compare_operator','main.py',1339),
  ('compare_operator -> EQUAL EQUAL','compare_operator',2,'p_compare_operator','main.py',1340),
  ('compare_operator -> NOTEQUAL EQUAL','compare_operator',2,'p_compare_operator','main.py',1341),
  ('string_calculate -> string_calculate stringoperator STRING','string_calculate',3,'p_string_calculate','main.py',1352),
  ('string_calculate -> STRING','string_calculate',1,'p_string_calculate','main.py',1353),
  ('stringoperator -> PLUS','stringoperator',1,'p_stringOperator','main.py',1362),
  ('calculate -> calculate PLUS calculate','calculate',3,'p_calculate_binop','main.py',1367),
  ('calculate -> calculate MINUS calculate','calculate',3,'p_calculate_binop','main.py',1368),
  ('calculate -> calculate MUL calculate','calculate',3,'p_calculate_binop','main.py',1369),
  ('calculate -> calculate DIV calculate','calculate',3,'p_calculate_binop','main.py',1370),
  ('calculate -> MINUS calculate','calculate',2,'p_calculate_uminus','main.py',1377),
  ('calculate -> LSB calculate RSB','calculate',3,'p_calculate_group','main.py',1381),
  ('calculate -> INT','calculate',1,'p_calculate_number','main.py',1385),
  ('calculate -> IDENTIFIER','calculate',1,'p_calculate_identifier','main.py',1390),
  ('empty -> <empty>','empty',0,'p_empty','main.py',1449),
]
