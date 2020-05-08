
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftMULDIVrightUMINUSCOLON DIV ELSE EQUAL FLOAT FUNCTION IDENTIFIER IF INT LB LMB LSB MINUS MUL PLUS RB RMB RSB SEMI STRING VAR\n    root : expression\n    \n    expression : expression variable_declaration SEMI\n        | expression variable_value_change SEMI\n    \n    expression : expression if_statement\n    \n    expression : variable_declaration SEMI\n        | variable_value_change SEMI\n    \n    expression : if_statement\n    \n    expression : empty\n    \n    if_statement : if_statement_head if_statement_body\n    \n    if_statement_head : IF LSB condition RSB\n    \n    if_statement_body : LMB expression RMB\n    \n    condition : condition LB calculate\n        | condition RB calculate\n    \n    condition : condition LB EQUAL calculate\n        | condition RB EQUAL calculate\n    \n    condition : condition EQUAL calculate\n    \n    condition : calculate\n    \n    variable_value_change : IDENTIFIER EQUAL calculate\n    \n    variable_declaration : VAR IDENTIFIER EQUAL calculate\n    \n    variable_declaration : VAR IDENTIFIER\n    calculate : calculate PLUS calculatecalculate : calculate MINUS calculatecalculate : MINUS calculate %prec UMINUS\n    calculate : calculate MUL calculate\n        | calculate DIV calculate\n    \n    calculate : INT\n        | FLOAT\n        | STRING\n    \n    calculate : IDENTIFIER\n    calculate : LSB calculate RSBempty : '
    
_lr_action_items = {'VAR':([0,2,5,6,13,14,15,18,19,21,22,31,41,],[7,7,-7,-8,-4,-5,-6,-9,7,-2,-3,7,-11,]),'IDENTIFIER':([0,2,5,6,7,13,14,15,17,18,19,20,21,22,23,26,30,31,35,36,37,38,41,43,44,45,52,54,],[8,8,-7,-8,16,-4,-5,-6,24,-9,8,24,-2,-3,24,24,24,8,24,24,24,24,-11,24,24,24,24,24,]),'IF':([0,2,5,6,13,14,15,18,19,21,22,31,41,],[10,10,-7,-8,-4,-5,-6,-9,10,-2,-3,10,-11,]),'$end':([0,1,2,5,6,13,14,15,18,21,22,41,],[-31,0,-1,-7,-8,-4,-5,-6,-9,-2,-3,-11,]),'SEMI':([3,4,11,12,16,24,25,27,28,29,34,39,46,47,48,49,50,],[14,15,21,22,-20,-29,-18,-26,-27,-28,-19,-23,-21,-22,-24,-25,-30,]),'RMB':([5,6,13,14,15,18,19,21,22,31,41,],[-7,-8,-4,-5,-6,-9,-31,-2,-3,41,-11,]),'EQUAL':([8,16,24,27,28,29,32,33,39,43,44,46,47,48,49,50,51,53,55,56,57,],[17,23,-29,-26,-27,-28,45,-17,-23,52,54,-21,-22,-24,-25,-30,-12,-13,-16,-14,-15,]),'LMB':([9,42,],[19,-10,]),'LSB':([10,17,20,23,26,30,35,36,37,38,43,44,45,52,54,],[20,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'MINUS':([17,20,23,24,25,26,27,28,29,30,33,34,35,36,37,38,39,40,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,],[26,26,26,-29,36,26,-26,-27,-28,26,36,36,26,26,26,26,-23,36,26,26,26,-21,-22,-24,-25,-30,36,26,36,26,36,36,36,]),'INT':([17,20,23,26,30,35,36,37,38,43,44,45,52,54,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'FLOAT':([17,20,23,26,30,35,36,37,38,43,44,45,52,54,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'STRING':([17,20,23,26,30,35,36,37,38,43,44,45,52,54,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'PLUS':([24,25,27,28,29,33,34,39,40,46,47,48,49,50,51,53,55,56,57,],[-29,35,-26,-27,-28,35,35,-23,35,-21,-22,-24,-25,-30,35,35,35,35,35,]),'MUL':([24,25,27,28,29,33,34,39,40,46,47,48,49,50,51,53,55,56,57,],[-29,37,-26,-27,-28,37,37,-23,37,37,37,-24,-25,-30,37,37,37,37,37,]),'DIV':([24,25,27,28,29,33,34,39,40,46,47,48,49,50,51,53,55,56,57,],[-29,38,-26,-27,-28,38,38,-23,38,38,38,-24,-25,-30,38,38,38,38,38,]),'RSB':([24,27,28,29,32,33,39,40,46,47,48,49,50,51,53,55,56,57,],[-29,-26,-27,-28,42,-17,-23,50,-21,-22,-24,-25,-30,-12,-13,-16,-14,-15,]),'LB':([24,27,28,29,32,33,39,46,47,48,49,50,51,53,55,56,57,],[-29,-26,-27,-28,43,-17,-23,-21,-22,-24,-25,-30,-12,-13,-16,-14,-15,]),'RB':([24,27,28,29,32,33,39,46,47,48,49,50,51,53,55,56,57,],[-29,-26,-27,-28,44,-17,-23,-21,-22,-24,-25,-30,-12,-13,-16,-14,-15,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'root':([0,],[1,]),'expression':([0,19,],[2,31,]),'variable_declaration':([0,2,19,31,],[3,11,3,11,]),'variable_value_change':([0,2,19,31,],[4,12,4,12,]),'if_statement':([0,2,19,31,],[5,13,5,13,]),'empty':([0,19,],[6,6,]),'if_statement_head':([0,2,19,31,],[9,9,9,9,]),'if_statement_body':([9,],[18,]),'calculate':([17,20,23,26,30,35,36,37,38,43,44,45,52,54,],[25,33,34,39,40,46,47,48,49,51,53,55,56,57,]),'condition':([20,],[32,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> root","S'",1,None,None,None),
  ('root -> expression','root',1,'p_root','main.py',129),
  ('expression -> expression variable_declaration SEMI','expression',3,'p_expression_variable','main.py',140),
  ('expression -> expression variable_value_change SEMI','expression',3,'p_expression_variable','main.py',141),
  ('expression -> expression if_statement','expression',2,'p_expression_if_statement','main.py',158),
  ('expression -> variable_declaration SEMI','expression',2,'p_expression_variable_2','main.py',171),
  ('expression -> variable_value_change SEMI','expression',2,'p_expression_variable_2','main.py',172),
  ('expression -> if_statement','expression',1,'p_expression_if_statement_2','main.py',183),
  ('expression -> empty','expression',1,'p_expression_empty','main.py',193),
  ('if_statement -> if_statement_head if_statement_body','if_statement',2,'p_if_statement','main.py',203),
  ('if_statement_head -> IF LSB condition RSB','if_statement_head',4,'p_if_statement_head','main.py',210),
  ('if_statement_body -> LMB expression RMB','if_statement_body',3,'p_if_statement_body','main.py',216),
  ('condition -> condition LB calculate','condition',3,'p_condition','main.py',227),
  ('condition -> condition RB calculate','condition',3,'p_condition','main.py',228),
  ('condition -> condition LB EQUAL calculate','condition',4,'p_condition_2','main.py',234),
  ('condition -> condition RB EQUAL calculate','condition',4,'p_condition_2','main.py',235),
  ('condition -> condition EQUAL calculate','condition',3,'p_condition_3','main.py',241),
  ('condition -> calculate','condition',1,'p_condition_4','main.py',247),
  ('variable_value_change -> IDENTIFIER EQUAL calculate','variable_value_change',3,'p_variable_value_change','main.py',255),
  ('variable_declaration -> VAR IDENTIFIER EQUAL calculate','variable_declaration',4,'p_variable_declaration_2','main.py',280),
  ('variable_declaration -> VAR IDENTIFIER','variable_declaration',2,'p_variable_declaration_1','main.py',296),
  ('calculate -> calculate PLUS calculate','calculate',3,'p_add','main.py',325),
  ('calculate -> calculate MINUS calculate','calculate',3,'p_sub','main.py',340),
  ('calculate -> MINUS calculate','calculate',2,'p_calculate2uminus','main.py',344),
  ('calculate -> calculate MUL calculate','calculate',3,'p_mul_div','main.py',349),
  ('calculate -> calculate DIV calculate','calculate',3,'p_mul_div','main.py',350),
  ('calculate -> INT','calculate',1,'p_calculate2num','main.py',361),
  ('calculate -> FLOAT','calculate',1,'p_calculate2num','main.py',362),
  ('calculate -> STRING','calculate',1,'p_calculate2num','main.py',363),
  ('calculate -> IDENTIFIER','calculate',1,'p_calculate2str','main.py',369),
  ('calculate -> LSB calculate RSB','calculate',3,'p_parens','main.py',377),
  ('empty -> <empty>','empty',0,'p_empty','main.py',383),
]
