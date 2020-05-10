
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftMULDIVrightUMINUSCOLON COMMA DIV ELSE EQUAL FLOAT FOR FUNCTION IDENTIFIER IF IN INT LB LIST LMB LSB MINUS MUL PLUS RB REPEAT RMB RSB SEMI STRING VAR WHILE\n    root : expression\n    \n    expression : expression variable_declaration SEMI\n        | expression variable_value_change SEMI\n    \n    expression : expression if_statement\n    \n    expression : expression function\n        | expression function_call SEMI\n    \n    expression : expression repeat\n    \n    expression : expression for\n    \n    expression : variable_declaration SEMI\n        | variable_value_change SEMI\n    \n    expression : if_statement\n    \n    expression : function\n        | function_call\n    \n    expression : repeat\n    \n    expression : for\n    \n    expression : empty\n    \n    for : for_head for_body\n    \n    for_head : FOR LSB IDENTIFIER IN IDENTIFIER RSB\n    \n    for_body : LMB expression RMB\n    \n    repeat : repeat_head repeat_body\n    \n    repeat_head : REPEAT LSB calculate RSB\n    \n    repeat_body : LMB expression RMB\n    \n    function : function_head function_body\n    \n    function_head : FUNCTION IDENTIFIER LSB empty RSB\n        | FUNCTION IDENTIFIER LSB parameter RSB\n    \n    function_body : LMB expression RMB\n    \n    function_call : IDENTIFIER LSB parameter RSB\n    \n    parameter : parameter COMMA calculate\n    \n    parameter : calculate\n        | empty\n    \n    if_statement : if_statement_head if_statement_body\n    \n    if_statement_head : IF LSB condition RSB\n    \n    if_statement_body : LMB expression RMB\n    \n    condition : condition LB calculate\n        | condition RB calculate\n    \n    condition : condition LB EQUAL calculate\n        | condition RB EQUAL calculate\n    \n    condition : condition EQUAL calculate\n    \n    condition : calculate\n    \n    variable_value_change : IDENTIFIER EQUAL calculate\n    \n    variable_declaration : VAR IDENTIFIER EQUAL calculate\n    \n    variable_declaration : VAR IDENTIFIER\n    calculate : calculate PLUS calculatecalculate : calculate MINUS calculatecalculate : MINUS calculate %prec UMINUS\n    calculate : calculate MUL calculate\n        | calculate DIV calculate\n    \n    calculate : INT\n        | FLOAT\n        | STRING\n    \n    calculate : IDENTIFIER\n    calculate : LSB calculate RSBempty : '
    
_lr_action_items = {'VAR':([0,2,5,6,7,8,9,10,23,24,26,27,28,29,33,34,35,36,37,38,39,40,45,46,47,59,60,61,62,75,77,78,79,80,],[11,11,-11,-12,-13,-14,-15,-16,-4,-5,-7,-8,-9,-10,-31,11,-23,11,-20,11,-17,11,-2,-3,-6,11,11,11,11,-27,-33,-26,-22,-19,]),'IDENTIFIER':([0,2,5,6,7,8,9,10,11,18,23,24,26,27,28,29,31,32,33,34,35,36,37,38,39,40,41,43,44,45,46,47,48,51,55,59,60,61,62,65,69,70,71,72,75,76,77,78,79,80,82,83,84,88,96,98,],[12,12,-11,-12,-13,-14,-15,-16,30,42,-4,-5,-7,-8,-9,-10,49,49,-31,12,-23,12,-20,12,-17,12,49,49,67,-2,-3,-6,49,49,49,12,12,12,12,49,49,49,49,49,-27,49,-33,-26,-22,-19,49,49,49,102,49,49,]),'IF':([0,2,5,6,7,8,9,10,23,24,26,27,28,29,33,34,35,36,37,38,39,40,45,46,47,59,60,61,62,75,77,78,79,80,],[17,17,-11,-12,-13,-14,-15,-16,-4,-5,-7,-8,-9,-10,-31,17,-23,17,-20,17,-17,17,-2,-3,-6,17,17,17,17,-27,-33,-26,-22,-19,]),'FUNCTION':([0,2,5,6,7,8,9,10,23,24,26,27,28,29,33,34,35,36,37,38,39,40,45,46,47,59,60,61,62,75,77,78,79,80,],[18,18,-11,-12,-13,-14,-15,-16,-4,-5,-7,-8,-9,-10,-31,18,-23,18,-20,18,-17,18,-2,-3,-6,18,18,18,18,-27,-33,-26,-22,-19,]),'REPEAT':([0,2,5,6,7,8,9,10,23,24,26,27,28,29,33,34,35,36,37,38,39,40,45,46,47,59,60,61,62,75,77,78,79,80,],[19,19,-11,-12,-13,-14,-15,-16,-4,-5,-7,-8,-9,-10,-31,19,-23,19,-20,19,-17,19,-2,-3,-6,19,19,19,19,-27,-33,-26,-22,-19,]),'FOR':([0,2,5,6,7,8,9,10,23,24,26,27,28,29,33,34,35,36,37,38,39,40,45,46,47,59,60,61,62,75,77,78,79,80,],[20,20,-11,-12,-13,-14,-15,-16,-4,-5,-7,-8,-9,-10,-31,20,-23,20,-20,20,-17,20,-2,-3,-6,20,20,20,20,-27,-33,-26,-22,-19,]),'$end':([0,1,2,5,6,7,8,9,10,23,24,26,27,28,29,33,35,37,39,45,46,47,75,77,78,79,80,],[-53,0,-1,-11,-12,-13,-14,-15,-16,-4,-5,-7,-8,-9,-10,-31,-23,-20,-17,-2,-3,-6,-27,-33,-26,-22,-19,]),'SEMI':([3,4,21,22,25,30,49,50,52,53,54,68,73,75,89,90,91,92,93,],[28,29,45,46,47,-42,-51,-40,-48,-49,-50,-41,-45,-27,-43,-44,-46,-47,-52,]),'RMB':([5,6,7,8,9,10,23,24,26,27,28,29,33,34,35,36,37,38,39,40,45,46,47,59,60,61,62,75,77,78,79,80,],[-11,-12,-13,-14,-15,-16,-4,-5,-7,-8,-9,-10,-31,-53,-23,-53,-20,-53,-17,-53,-2,-3,-6,77,78,79,80,-27,-33,-26,-22,-19,]),'EQUAL':([12,30,49,52,53,54,63,64,73,82,83,89,90,91,92,93,95,97,99,103,104,],[31,48,-51,-48,-49,-50,84,-39,-45,96,98,-43,-44,-46,-47,-52,-34,-35,-38,-36,-37,]),'LSB':([12,17,19,20,31,32,41,42,43,48,51,55,65,69,70,71,72,76,82,83,84,96,98,],[32,41,43,44,55,55,55,65,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,]),'LMB':([13,14,15,16,81,87,100,101,105,],[34,36,38,40,-32,-21,-24,-25,-18,]),'MINUS':([31,32,41,43,48,49,50,51,52,53,54,55,57,64,65,66,68,69,70,71,72,73,74,76,82,83,84,89,90,91,92,93,94,95,96,97,98,99,103,104,],[51,51,51,51,51,-51,70,51,-48,-49,-50,51,70,70,51,70,70,51,51,51,51,-45,70,51,51,51,51,-43,-44,-46,-47,-52,70,70,51,70,51,70,70,70,]),'INT':([31,32,41,43,48,51,55,65,69,70,71,72,76,82,83,84,96,98,],[52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,]),'FLOAT':([31,32,41,43,48,51,55,65,69,70,71,72,76,82,83,84,96,98,],[53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'STRING':([31,32,41,43,48,51,55,65,69,70,71,72,76,82,83,84,96,98,],[54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,]),'RSB':([32,49,52,53,54,56,57,58,63,64,65,66,73,74,85,86,89,90,91,92,93,94,95,97,99,102,103,104,],[-53,-51,-48,-49,-50,75,-29,-30,81,-39,-53,87,-45,93,100,101,-43,-44,-46,-47,-52,-28,-34,-35,-38,105,-36,-37,]),'COMMA':([32,49,52,53,54,56,57,58,65,73,85,86,89,90,91,92,93,94,],[-53,-51,-48,-49,-50,76,-29,-30,-53,-45,-30,76,-43,-44,-46,-47,-52,-28,]),'PLUS':([49,50,52,53,54,57,64,66,68,73,74,89,90,91,92,93,94,95,97,99,103,104,],[-51,69,-48,-49,-50,69,69,69,69,-45,69,-43,-44,-46,-47,-52,69,69,69,69,69,69,]),'MUL':([49,50,52,53,54,57,64,66,68,73,74,89,90,91,92,93,94,95,97,99,103,104,],[-51,71,-48,-49,-50,71,71,71,71,-45,71,71,71,-46,-47,-52,71,71,71,71,71,71,]),'DIV':([49,50,52,53,54,57,64,66,68,73,74,89,90,91,92,93,94,95,97,99,103,104,],[-51,72,-48,-49,-50,72,72,72,72,-45,72,72,72,-46,-47,-52,72,72,72,72,72,72,]),'LB':([49,52,53,54,63,64,73,89,90,91,92,93,95,97,99,103,104,],[-51,-48,-49,-50,82,-39,-45,-43,-44,-46,-47,-52,-34,-35,-38,-36,-37,]),'RB':([49,52,53,54,63,64,73,89,90,91,92,93,95,97,99,103,104,],[-51,-48,-49,-50,83,-39,-45,-43,-44,-46,-47,-52,-34,-35,-38,-36,-37,]),'IN':([67,],[88,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'root':([0,],[1,]),'expression':([0,34,36,38,40,],[2,59,60,61,62,]),'variable_declaration':([0,2,34,36,38,40,59,60,61,62,],[3,21,3,3,3,3,21,21,21,21,]),'variable_value_change':([0,2,34,36,38,40,59,60,61,62,],[4,22,4,4,4,4,22,22,22,22,]),'if_statement':([0,2,34,36,38,40,59,60,61,62,],[5,23,5,5,5,5,23,23,23,23,]),'function':([0,2,34,36,38,40,59,60,61,62,],[6,24,6,6,6,6,24,24,24,24,]),'function_call':([0,2,34,36,38,40,59,60,61,62,],[7,25,7,7,7,7,25,25,25,25,]),'repeat':([0,2,34,36,38,40,59,60,61,62,],[8,26,8,8,8,8,26,26,26,26,]),'for':([0,2,34,36,38,40,59,60,61,62,],[9,27,9,9,9,9,27,27,27,27,]),'empty':([0,32,34,36,38,40,65,],[10,58,10,10,10,10,85,]),'if_statement_head':([0,2,34,36,38,40,59,60,61,62,],[13,13,13,13,13,13,13,13,13,13,]),'function_head':([0,2,34,36,38,40,59,60,61,62,],[14,14,14,14,14,14,14,14,14,14,]),'repeat_head':([0,2,34,36,38,40,59,60,61,62,],[15,15,15,15,15,15,15,15,15,15,]),'for_head':([0,2,34,36,38,40,59,60,61,62,],[16,16,16,16,16,16,16,16,16,16,]),'if_statement_body':([13,],[33,]),'function_body':([14,],[35,]),'repeat_body':([15,],[37,]),'for_body':([16,],[39,]),'calculate':([31,32,41,43,48,51,55,65,69,70,71,72,76,82,83,84,96,98,],[50,57,64,66,68,73,74,57,89,90,91,92,94,95,97,99,103,104,]),'parameter':([32,65,],[56,86,]),'condition':([41,],[63,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> root","S'",1,None,None,None),
  ('root -> expression','root',1,'p_root','main.py',142),
  ('expression -> expression variable_declaration SEMI','expression',3,'p_expression_variable','main.py',156),
  ('expression -> expression variable_value_change SEMI','expression',3,'p_expression_variable','main.py',157),
  ('expression -> expression if_statement','expression',2,'p_expression_if_statement','main.py',174),
  ('expression -> expression function','expression',2,'p_expression_function','main.py',185),
  ('expression -> expression function_call SEMI','expression',3,'p_expression_function','main.py',186),
  ('expression -> expression repeat','expression',2,'p_expression_repeat','main.py',192),
  ('expression -> expression for','expression',2,'p_expression_for','main.py',198),
  ('expression -> variable_declaration SEMI','expression',2,'p_expression_variable_2','main.py',206),
  ('expression -> variable_value_change SEMI','expression',2,'p_expression_variable_2','main.py',207),
  ('expression -> if_statement','expression',1,'p_expression_if_statement_2','main.py',218),
  ('expression -> function','expression',1,'p_expression_function_2','main.py',226),
  ('expression -> function_call','expression',1,'p_expression_function_2','main.py',227),
  ('expression -> repeat','expression',1,'p_expression_repeat_2','main.py',233),
  ('expression -> for','expression',1,'p_expression_for_2','main.py',239),
  ('expression -> empty','expression',1,'p_expression_empty','main.py',247),
  ('for -> for_head for_body','for',2,'p_for','main.py',256),
  ('for_head -> FOR LSB IDENTIFIER IN IDENTIFIER RSB','for_head',6,'p_for_head','main.py',264),
  ('for_body -> LMB expression RMB','for_body',3,'p_for_body','main.py',270),
  ('repeat -> repeat_head repeat_body','repeat',2,'p_repeat','main.py',283),
  ('repeat_head -> REPEAT LSB calculate RSB','repeat_head',4,'p_repeat_head','main.py',291),
  ('repeat_body -> LMB expression RMB','repeat_body',3,'p_repeat_body','main.py',297),
  ('function -> function_head function_body','function',2,'p_function','main.py',310),
  ('function_head -> FUNCTION IDENTIFIER LSB empty RSB','function_head',5,'p_function_head','main.py',318),
  ('function_head -> FUNCTION IDENTIFIER LSB parameter RSB','function_head',5,'p_function_head','main.py',319),
  ('function_body -> LMB expression RMB','function_body',3,'p_function_body','main.py',328),
  ('function_call -> IDENTIFIER LSB parameter RSB','function_call',4,'p_function_call','main.py',339),
  ('parameter -> parameter COMMA calculate','parameter',3,'p_parameter','main.py',347),
  ('parameter -> calculate','parameter',1,'p_parameter_2','main.py',353),
  ('parameter -> empty','parameter',1,'p_parameter_2','main.py',354),
  ('if_statement -> if_statement_head if_statement_body','if_statement',2,'p_if_statement','main.py',365),
  ('if_statement_head -> IF LSB condition RSB','if_statement_head',4,'p_if_statement_head','main.py',373),
  ('if_statement_body -> LMB expression RMB','if_statement_body',3,'p_if_statement_body','main.py',379),
  ('condition -> condition LB calculate','condition',3,'p_condition','main.py',390),
  ('condition -> condition RB calculate','condition',3,'p_condition','main.py',391),
  ('condition -> condition LB EQUAL calculate','condition',4,'p_condition_2','main.py',397),
  ('condition -> condition RB EQUAL calculate','condition',4,'p_condition_2','main.py',398),
  ('condition -> condition EQUAL calculate','condition',3,'p_condition_3','main.py',404),
  ('condition -> calculate','condition',1,'p_condition_4','main.py',410),
  ('variable_value_change -> IDENTIFIER EQUAL calculate','variable_value_change',3,'p_variable_value_change','main.py',418),
  ('variable_declaration -> VAR IDENTIFIER EQUAL calculate','variable_declaration',4,'p_variable_declaration_2','main.py',443),
  ('variable_declaration -> VAR IDENTIFIER','variable_declaration',2,'p_variable_declaration_1','main.py',459),
  ('calculate -> calculate PLUS calculate','calculate',3,'p_add','main.py',488),
  ('calculate -> calculate MINUS calculate','calculate',3,'p_sub','main.py',512),
  ('calculate -> MINUS calculate','calculate',2,'p_calculate2uminus','main.py',516),
  ('calculate -> calculate MUL calculate','calculate',3,'p_mul_div','main.py',521),
  ('calculate -> calculate DIV calculate','calculate',3,'p_mul_div','main.py',522),
  ('calculate -> INT','calculate',1,'p_calculate2num','main.py',533),
  ('calculate -> FLOAT','calculate',1,'p_calculate2num','main.py',534),
  ('calculate -> STRING','calculate',1,'p_calculate2num','main.py',535),
  ('calculate -> IDENTIFIER','calculate',1,'p_calculate2str','main.py',541),
  ('calculate -> LSB calculate RSB','calculate',3,'p_parens','main.py',549),
  ('empty -> <empty>','empty',0,'p_empty','main.py',555),
]
