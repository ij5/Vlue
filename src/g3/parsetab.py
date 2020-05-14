
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftMULDIVrightUMINUSCOLON COMMA DIV ELSE EQUAL FLOAT FOR FUNCTION IDENTIFIER IF IN INT LB LIST LMB LSB MINUS MUL PLUS RB REPEAT RMB RSB SEMI STRING USE VAR WHILE\n    root : expression\n    \n    expression : expression variable_declaration SEMI\n        | expression variable_value_change SEMI\n    \n    expression : expression if_statement\n    \n    expression : expression function\n        | expression function_call SEMI\n    \n    expression : expression repeat\n    \n    expression : expression for\n    \n    expression : expression while\n    \n    expression : expression use\n    \n    expression : variable_declaration SEMI\n        | variable_value_change SEMI\n    \n    expression : if_statement\n    \n    expression : function\n        | function_call\n    \n    expression : repeat\n    \n    expression : for\n    \n    expression : while\n    \n    expression : use\n    \n    expression : empty\n    \n    for : for_head for_body\n    \n    for_head : FOR LSB IDENTIFIER IN IDENTIFIER RSB\n    \n    for_body : LMB expression RMB\n    \n    while : while_head while_body\n    \n    while_head : WHILE LSB condition RSB\n    \n    while_body : LMB expression RMB\n    \n    repeat : repeat_head repeat_body\n    \n    repeat_head : REPEAT LSB calculate RSB\n    \n    repeat_body : LMB expression RMB\n    \n    function : function_head function_body\n    \n    function_head : FUNCTION IDENTIFIER LSB empty RSB\n        | FUNCTION IDENTIFIER LSB parameter RSB\n    \n    function_body : LMB expression RMB\n    \n    function_call : IDENTIFIER LSB parameter RSB\n    \n    parameter : parameter COMMA calculate\n    \n    parameter : calculate\n        | empty\n    \n    if_statement : if_statement_1 if_statement_2 if_statement_3\n        | if_statement_1 if_statement_2\n        | if_statement_1 if_statement_3\n    \n    if_statement_1 : IF LSB condition RSB LMB expression RMB\n    \n    if_statement_2 : ELSE IF LSB condition RSB LMB expression RMB\n        | if_statement_2 ELSE IF LSB condition RSB LMB expression RMB\n    \n    if_statement_3 : ELSE LMB expression RMB\n    \n    condition : condition LB calculate\n        | condition RB calculate\n    \n    condition : condition LB EQUAL calculate\n        | condition RB EQUAL calculate\n    \n    condition : condition EQUAL calculate\n    \n    condition : calculate\n    \n    use : USE IDENTIFIER\n    \n    variable_value_change : IDENTIFIER EQUAL LIST\n    \n    variable_value_change : IDENTIFIER EQUAL calculate\n    \n    variable_declaration : VAR IDENTIFIER EQUAL LIST\n    \n    variable_declaration : VAR IDENTIFIER EQUAL calculate\n    \n    variable_declaration : VAR IDENTIFIER\n    calculate : calculate PLUS calculatecalculate : calculate MINUS calculatecalculate : MINUS calculate %prec UMINUS\n    calculate : calculate MUL calculate\n        | calculate DIV calculate\n    \n    calculate : INT\n        | FLOAT\n        | STRING\n    \n    calculate : IDENTIFIER\n    calculate : LSB calculate RSBempty : '
    
_lr_action_items = {'VAR':([0,2,5,6,7,8,9,10,11,12,28,29,31,32,33,34,35,36,40,41,43,44,45,46,47,48,49,50,51,57,58,59,72,75,76,77,78,79,94,98,99,100,101,102,120,121,132,137,139,140,141,142,143,],[13,13,-13,-14,-15,-16,-17,-18,-19,-20,-4,-5,-7,-8,-9,-10,-11,-12,-39,-40,-30,13,-27,13,-21,13,-24,13,-51,-2,-3,-6,-38,13,13,13,13,13,-34,13,-33,-29,-23,-26,-44,13,13,13,13,13,13,-42,-43,]),'IDENTIFIER':([0,2,5,6,7,8,9,10,11,12,13,20,22,28,29,31,32,33,34,35,36,38,39,40,41,43,44,45,46,47,48,49,50,51,52,54,55,56,57,58,59,60,64,68,72,75,76,77,78,79,82,88,89,90,91,94,95,97,98,99,100,101,102,104,105,106,110,118,120,121,123,125,132,137,139,140,141,142,143,],[14,14,-13,-14,-15,-16,-17,-18,-19,-20,37,51,53,-4,-5,-7,-8,-9,-10,-11,-12,61,61,-39,-40,-30,14,-27,14,-21,14,-24,14,-51,61,61,84,61,-2,-3,-6,61,61,61,-38,14,14,14,14,14,61,61,61,61,61,-34,61,61,14,-33,-29,-23,-26,61,61,61,129,61,-44,14,61,61,14,14,14,14,14,-42,-43,]),'USE':([0,2,5,6,7,8,9,10,11,12,28,29,31,32,33,34,35,36,40,41,43,44,45,46,47,48,49,50,51,57,58,59,72,75,76,77,78,79,94,98,99,100,101,102,120,121,132,137,139,140,141,142,143,],[20,20,-13,-14,-15,-16,-17,-18,-19,-20,-4,-5,-7,-8,-9,-10,-11,-12,-39,-40,-30,20,-27,20,-21,20,-24,20,-51,-2,-3,-6,-38,20,20,20,20,20,-34,20,-33,-29,-23,-26,-44,20,20,20,20,20,20,-42,-43,]),'IF':([0,2,5,6,7,8,9,10,11,12,28,29,31,32,33,34,35,36,40,41,42,43,44,45,46,47,48,49,50,51,57,58,59,72,73,75,76,77,78,79,94,98,99,100,101,102,120,121,132,137,139,140,141,142,143,],[21,21,-13,-14,-15,-16,-17,-18,-19,-20,-4,-5,-7,-8,-9,-10,-11,-12,-39,-40,74,-30,21,-27,21,-21,21,-24,21,-51,-2,-3,-6,-38,96,21,21,21,21,21,-34,21,-33,-29,-23,-26,-44,21,21,21,21,21,21,-42,-43,]),'FUNCTION':([0,2,5,6,7,8,9,10,11,12,28,29,31,32,33,34,35,36,40,41,43,44,45,46,47,48,49,50,51,57,58,59,72,75,76,77,78,79,94,98,99,100,101,102,120,121,132,137,139,140,141,142,143,],[22,22,-13,-14,-15,-16,-17,-18,-19,-20,-4,-5,-7,-8,-9,-10,-11,-12,-39,-40,-30,22,-27,22,-21,22,-24,22,-51,-2,-3,-6,-38,22,22,22,22,22,-34,22,-33,-29,-23,-26,-44,22,22,22,22,22,22,-42,-43,]),'REPEAT':([0,2,5,6,7,8,9,10,11,12,28,29,31,32,33,34,35,36,40,41,43,44,45,46,47,48,49,50,51,57,58,59,72,75,76,77,78,79,94,98,99,100,101,102,120,121,132,137,139,140,141,142,143,],[23,23,-13,-14,-15,-16,-17,-18,-19,-20,-4,-5,-7,-8,-9,-10,-11,-12,-39,-40,-30,23,-27,23,-21,23,-24,23,-51,-2,-3,-6,-38,23,23,23,23,23,-34,23,-33,-29,-23,-26,-44,23,23,23,23,23,23,-42,-43,]),'FOR':([0,2,5,6,7,8,9,10,11,12,28,29,31,32,33,34,35,36,40,41,43,44,45,46,47,48,49,50,51,57,58,59,72,75,76,77,78,79,94,98,99,100,101,102,120,121,132,137,139,140,141,142,143,],[24,24,-13,-14,-15,-16,-17,-18,-19,-20,-4,-5,-7,-8,-9,-10,-11,-12,-39,-40,-30,24,-27,24,-21,24,-24,24,-51,-2,-3,-6,-38,24,24,24,24,24,-34,24,-33,-29,-23,-26,-44,24,24,24,24,24,24,-42,-43,]),'WHILE':([0,2,5,6,7,8,9,10,11,12,28,29,31,32,33,34,35,36,40,41,43,44,45,46,47,48,49,50,51,57,58,59,72,75,76,77,78,79,94,98,99,100,101,102,120,121,132,137,139,140,141,142,143,],[25,25,-13,-14,-15,-16,-17,-18,-19,-20,-4,-5,-7,-8,-9,-10,-11,-12,-39,-40,-30,25,-27,25,-21,25,-24,25,-51,-2,-3,-6,-38,25,25,25,25,25,-34,25,-33,-29,-23,-26,-44,25,25,25,25,25,25,-42,-43,]),'$end':([0,1,2,5,6,7,8,9,10,11,12,28,29,31,32,33,34,35,36,40,41,43,45,47,49,51,57,58,59,72,94,99,100,101,102,120,142,143,],[-67,0,-1,-13,-14,-15,-16,-17,-18,-19,-20,-4,-5,-7,-8,-9,-10,-11,-12,-39,-40,-30,-27,-21,-24,-51,-2,-3,-6,-38,-34,-33,-29,-23,-26,-44,-42,-43,]),'SEMI':([3,4,26,27,30,37,61,62,63,65,66,67,86,87,92,94,112,113,114,115,116,],[35,36,57,58,59,-56,-65,-52,-53,-62,-63,-64,-54,-55,-59,-34,-57,-58,-60,-61,-66,]),'RMB':([5,6,7,8,9,10,11,12,28,29,31,32,33,34,35,36,40,41,43,44,45,46,47,48,49,50,51,57,58,59,72,75,76,77,78,79,94,98,99,100,101,102,120,121,132,137,139,140,141,142,143,],[-13,-14,-15,-16,-17,-18,-19,-20,-4,-5,-7,-8,-9,-10,-11,-12,-39,-40,-30,-67,-27,-67,-21,-67,-24,-67,-51,-2,-3,-6,-38,-67,99,100,101,102,-34,120,-33,-29,-23,-26,-44,-67,138,-67,-67,142,143,-42,-43,]),'EQUAL':([14,37,61,65,66,67,80,81,85,92,104,105,112,113,114,115,116,119,122,124,126,130,133,134,],[38,60,-65,-62,-63,-64,106,-50,106,-59,123,125,-57,-58,-60,-61,-66,106,-45,-46,-49,106,-47,-48,]),'LSB':([14,21,23,24,25,38,39,52,53,54,56,60,64,68,74,82,88,89,90,91,95,96,97,104,105,106,118,123,125,],[39,52,54,55,56,68,68,68,82,68,68,68,68,68,97,68,68,68,68,68,68,118,68,68,68,68,68,68,68,]),'ELSE':([15,40,138,142,143,],[42,73,-41,-42,-43,]),'LMB':([16,17,18,19,42,73,103,109,111,127,128,131,135,136,],[44,46,48,50,75,75,121,-28,-25,-31,-32,137,-22,139,]),'LIST':([38,60,],[62,86,]),'MINUS':([38,39,52,54,56,60,61,63,64,65,66,67,68,70,81,82,83,87,88,89,90,91,92,93,95,97,104,105,106,112,113,114,115,116,117,118,122,123,124,125,126,133,134,],[64,64,64,64,64,64,-65,89,64,-62,-63,-64,64,89,89,64,89,89,64,64,64,64,-59,89,64,64,64,64,64,-57,-58,-60,-61,-66,89,64,89,64,89,64,89,89,89,]),'INT':([38,39,52,54,56,60,64,68,82,88,89,90,91,95,97,104,105,106,118,123,125,],[65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,]),'FLOAT':([38,39,52,54,56,60,64,68,82,88,89,90,91,95,97,104,105,106,118,123,125,],[66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,]),'STRING':([38,39,52,54,56,60,64,68,82,88,89,90,91,95,97,104,105,106,118,123,125,],[67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,]),'RSB':([39,61,65,66,67,69,70,71,80,81,82,83,85,92,93,107,108,112,113,114,115,116,117,119,122,124,126,129,130,133,134,],[-67,-65,-62,-63,-64,94,-36,-37,103,-50,-67,109,111,-59,116,127,128,-57,-58,-60,-61,-66,-35,131,-45,-46,-49,135,136,-47,-48,]),'COMMA':([39,61,65,66,67,69,70,71,82,92,107,108,112,113,114,115,116,117,],[-67,-65,-62,-63,-64,95,-36,-37,-67,-59,-37,95,-57,-58,-60,-61,-66,-35,]),'PLUS':([61,63,65,66,67,70,81,83,87,92,93,112,113,114,115,116,117,122,124,126,133,134,],[-65,88,-62,-63,-64,88,88,88,88,-59,88,-57,-58,-60,-61,-66,88,88,88,88,88,88,]),'MUL':([61,63,65,66,67,70,81,83,87,92,93,112,113,114,115,116,117,122,124,126,133,134,],[-65,90,-62,-63,-64,90,90,90,90,-59,90,90,90,-60,-61,-66,90,90,90,90,90,90,]),'DIV':([61,63,65,66,67,70,81,83,87,92,93,112,113,114,115,116,117,122,124,126,133,134,],[-65,91,-62,-63,-64,91,91,91,91,-59,91,91,91,-60,-61,-66,91,91,91,91,91,91,]),'LB':([61,65,66,67,80,81,85,92,112,113,114,115,116,119,122,124,126,130,133,134,],[-65,-62,-63,-64,104,-50,104,-59,-57,-58,-60,-61,-66,104,-45,-46,-49,104,-47,-48,]),'RB':([61,65,66,67,80,81,85,92,112,113,114,115,116,119,122,124,126,130,133,134,],[-65,-62,-63,-64,105,-50,105,-59,-57,-58,-60,-61,-66,105,-45,-46,-49,105,-47,-48,]),'IN':([84,],[110,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'root':([0,],[1,]),'expression':([0,44,46,48,50,75,121,137,139,],[2,76,77,78,79,98,132,140,141,]),'variable_declaration':([0,2,44,46,48,50,75,76,77,78,79,98,121,132,137,139,140,141,],[3,26,3,3,3,3,3,26,26,26,26,26,3,26,3,3,26,26,]),'variable_value_change':([0,2,44,46,48,50,75,76,77,78,79,98,121,132,137,139,140,141,],[4,27,4,4,4,4,4,27,27,27,27,27,4,27,4,4,27,27,]),'if_statement':([0,2,44,46,48,50,75,76,77,78,79,98,121,132,137,139,140,141,],[5,28,5,5,5,5,5,28,28,28,28,28,5,28,5,5,28,28,]),'function':([0,2,44,46,48,50,75,76,77,78,79,98,121,132,137,139,140,141,],[6,29,6,6,6,6,6,29,29,29,29,29,6,29,6,6,29,29,]),'function_call':([0,2,44,46,48,50,75,76,77,78,79,98,121,132,137,139,140,141,],[7,30,7,7,7,7,7,30,30,30,30,30,7,30,7,7,30,30,]),'repeat':([0,2,44,46,48,50,75,76,77,78,79,98,121,132,137,139,140,141,],[8,31,8,8,8,8,8,31,31,31,31,31,8,31,8,8,31,31,]),'for':([0,2,44,46,48,50,75,76,77,78,79,98,121,132,137,139,140,141,],[9,32,9,9,9,9,9,32,32,32,32,32,9,32,9,9,32,32,]),'while':([0,2,44,46,48,50,75,76,77,78,79,98,121,132,137,139,140,141,],[10,33,10,10,10,10,10,33,33,33,33,33,10,33,10,10,33,33,]),'use':([0,2,44,46,48,50,75,76,77,78,79,98,121,132,137,139,140,141,],[11,34,11,11,11,11,11,34,34,34,34,34,11,34,11,11,34,34,]),'empty':([0,39,44,46,48,50,75,82,121,137,139,],[12,71,12,12,12,12,12,107,12,12,12,]),'if_statement_1':([0,2,44,46,48,50,75,76,77,78,79,98,121,132,137,139,140,141,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'function_head':([0,2,44,46,48,50,75,76,77,78,79,98,121,132,137,139,140,141,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'repeat_head':([0,2,44,46,48,50,75,76,77,78,79,98,121,132,137,139,140,141,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'for_head':([0,2,44,46,48,50,75,76,77,78,79,98,121,132,137,139,140,141,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'while_head':([0,2,44,46,48,50,75,76,77,78,79,98,121,132,137,139,140,141,],[19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'if_statement_2':([15,],[40,]),'if_statement_3':([15,40,],[41,72,]),'function_body':([16,],[43,]),'repeat_body':([17,],[45,]),'for_body':([18,],[47,]),'while_body':([19,],[49,]),'calculate':([38,39,52,54,56,60,64,68,82,88,89,90,91,95,97,104,105,106,118,123,125,],[63,70,81,83,81,87,92,93,70,112,113,114,115,117,81,122,124,126,81,133,134,]),'parameter':([39,82,],[69,108,]),'condition':([52,56,97,118,],[80,85,119,130,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> root","S'",1,None,None,None),
  ('root -> expression','root',1,'p_root','main.py',144),
  ('expression -> expression variable_declaration SEMI','expression',3,'p_expression_variable','main.py',158),
  ('expression -> expression variable_value_change SEMI','expression',3,'p_expression_variable','main.py',159),
  ('expression -> expression if_statement','expression',2,'p_expression_if_statement','main.py',176),
  ('expression -> expression function','expression',2,'p_expression_function','main.py',187),
  ('expression -> expression function_call SEMI','expression',3,'p_expression_function','main.py',188),
  ('expression -> expression repeat','expression',2,'p_expression_repeat','main.py',194),
  ('expression -> expression for','expression',2,'p_expression_for','main.py',200),
  ('expression -> expression while','expression',2,'p_expression_while','main.py',206),
  ('expression -> expression use','expression',2,'p_expression_use','main.py',212),
  ('expression -> variable_declaration SEMI','expression',2,'p_expression_variable_2','main.py',220),
  ('expression -> variable_value_change SEMI','expression',2,'p_expression_variable_2','main.py',221),
  ('expression -> if_statement','expression',1,'p_expression_if_statement_2','main.py',232),
  ('expression -> function','expression',1,'p_expression_function_2','main.py',240),
  ('expression -> function_call','expression',1,'p_expression_function_2','main.py',241),
  ('expression -> repeat','expression',1,'p_expression_repeat_2','main.py',247),
  ('expression -> for','expression',1,'p_expression_for_2','main.py',253),
  ('expression -> while','expression',1,'p_expression_while_2','main.py',259),
  ('expression -> use','expression',1,'p_expression_use_2','main.py',265),
  ('expression -> empty','expression',1,'p_expression_empty','main.py',273),
  ('for -> for_head for_body','for',2,'p_for','main.py',282),
  ('for_head -> FOR LSB IDENTIFIER IN IDENTIFIER RSB','for_head',6,'p_for_head','main.py',290),
  ('for_body -> LMB expression RMB','for_body',3,'p_for_body','main.py',296),
  ('while -> while_head while_body','while',2,'p_while','main.py',307),
  ('while_head -> WHILE LSB condition RSB','while_head',4,'p_while_head','main.py',315),
  ('while_body -> LMB expression RMB','while_body',3,'p_while_body','main.py',321),
  ('repeat -> repeat_head repeat_body','repeat',2,'p_repeat','main.py',333),
  ('repeat_head -> REPEAT LSB calculate RSB','repeat_head',4,'p_repeat_head','main.py',341),
  ('repeat_body -> LMB expression RMB','repeat_body',3,'p_repeat_body','main.py',347),
  ('function -> function_head function_body','function',2,'p_function','main.py',360),
  ('function_head -> FUNCTION IDENTIFIER LSB empty RSB','function_head',5,'p_function_head','main.py',368),
  ('function_head -> FUNCTION IDENTIFIER LSB parameter RSB','function_head',5,'p_function_head','main.py',369),
  ('function_body -> LMB expression RMB','function_body',3,'p_function_body','main.py',378),
  ('function_call -> IDENTIFIER LSB parameter RSB','function_call',4,'p_function_call','main.py',389),
  ('parameter -> parameter COMMA calculate','parameter',3,'p_parameter','main.py',397),
  ('parameter -> calculate','parameter',1,'p_parameter_2','main.py',403),
  ('parameter -> empty','parameter',1,'p_parameter_2','main.py',404),
  ('if_statement -> if_statement_1 if_statement_2 if_statement_3','if_statement',3,'p_if_statement','main.py',415),
  ('if_statement -> if_statement_1 if_statement_2','if_statement',2,'p_if_statement','main.py',416),
  ('if_statement -> if_statement_1 if_statement_3','if_statement',2,'p_if_statement','main.py',417),
  ('if_statement_1 -> IF LSB condition RSB LMB expression RMB','if_statement_1',7,'p_if_statement_1','main.py',424),
  ('if_statement_2 -> ELSE IF LSB condition RSB LMB expression RMB','if_statement_2',8,'p_if_statement_2','main.py',431),
  ('if_statement_2 -> if_statement_2 ELSE IF LSB condition RSB LMB expression RMB','if_statement_2',9,'p_if_statement_2','main.py',432),
  ('if_statement_3 -> ELSE LMB expression RMB','if_statement_3',4,'p_if_statement_3','main.py',439),
  ('condition -> condition LB calculate','condition',3,'p_condition','main.py',448),
  ('condition -> condition RB calculate','condition',3,'p_condition','main.py',449),
  ('condition -> condition LB EQUAL calculate','condition',4,'p_condition_2','main.py',455),
  ('condition -> condition RB EQUAL calculate','condition',4,'p_condition_2','main.py',456),
  ('condition -> condition EQUAL calculate','condition',3,'p_condition_3','main.py',462),
  ('condition -> calculate','condition',1,'p_condition_4','main.py',468),
  ('use -> USE IDENTIFIER','use',2,'p_use','main.py',478),
  ('variable_value_change -> IDENTIFIER EQUAL LIST','variable_value_change',3,'p_variable_value_change_list','main.py',495),
  ('variable_value_change -> IDENTIFIER EQUAL calculate','variable_value_change',3,'p_variable_value_change','main.py',501),
  ('variable_declaration -> VAR IDENTIFIER EQUAL LIST','variable_declaration',4,'p_variable_declaration_list','main.py',527),
  ('variable_declaration -> VAR IDENTIFIER EQUAL calculate','variable_declaration',4,'p_variable_declaration_2','main.py',533),
  ('variable_declaration -> VAR IDENTIFIER','variable_declaration',2,'p_variable_declaration_1','main.py',549),
  ('calculate -> calculate PLUS calculate','calculate',3,'p_add','main.py',578),
  ('calculate -> calculate MINUS calculate','calculate',3,'p_sub','main.py',614),
  ('calculate -> MINUS calculate','calculate',2,'p_calculate2uminus','main.py',618),
  ('calculate -> calculate MUL calculate','calculate',3,'p_mul_div','main.py',623),
  ('calculate -> calculate DIV calculate','calculate',3,'p_mul_div','main.py',624),
  ('calculate -> INT','calculate',1,'p_calculate2num','main.py',635),
  ('calculate -> FLOAT','calculate',1,'p_calculate2num','main.py',636),
  ('calculate -> STRING','calculate',1,'p_calculate2num','main.py',637),
  ('calculate -> IDENTIFIER','calculate',1,'p_calculate2str','main.py',643),
  ('calculate -> LSB calculate RSB','calculate',3,'p_parens','main.py',651),
  ('empty -> <empty>','empty',0,'p_empty','main.py',657),
]
