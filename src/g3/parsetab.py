
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftMULDIVrightUMINUSCOLON DIV ELSE EQUAL FLOAT IDENTIFIER IF IF INT LB LMB LSB MINUS MUL PLUS RB RMB RSB SEMI STRING VAR\n    expression : expression variable_declaration SEMI\n        | expression variable_value_change SEMI\n        | expression if_statement SEMI\n    \n    expression : variable_declaration SEMI\n        | variable_value_change SEMI\n        | if_statement SEMI\n    \n    expression : empty\n    \n    if_statement : if_statement_head if_statement_body\n    \n    if_statement_head : IF LSB condition RSB\n    \n    if_statement_body : LMB expression RMB\n    \n    condition : condition LB calculate\n        | condition RB calculate\n    \n    condition : condition LB EQUAL calculate\n        | condition RB EQUAL calculate\n    \n    condition : condition EQUAL calculate\n    \n    condition : calculate\n    \n    variable_value_change : IDENTIFIER EQUAL calculate\n    \n    variable_declaration : VAR IDENTIFIER EQUAL calculate\n    \n    variable_declaration : VAR IDENTIFIER\n    calculate : calculate PLUS calculatecalculate : calculate MINUS calculatecalculate : MINUS calculate %prec UMINUS\n    calculate : calculate MUL calculate\n        | calculate DIV calculate\n    \n    calculate : INT\n        | FLOAT\n        | STRING\n    \n    calculate : IDENTIFIER\n    calculate : LSB calculate RSBempty : '
    
_lr_action_items = {'VAR':([0,1,5,13,14,15,19,21,22,23,32,],[6,6,-7,-4,-5,-6,6,-1,-2,-3,6,]),'IDENTIFIER':([0,1,5,6,13,14,15,17,19,20,21,22,23,24,27,31,32,36,37,38,39,44,45,46,53,55,],[7,7,-7,16,-4,-5,-6,25,7,25,-1,-2,-3,25,25,25,7,25,25,25,25,25,25,25,25,25,]),'IF':([0,1,5,13,14,15,19,21,22,23,32,],[9,9,-7,-4,-5,-6,9,-1,-2,-3,9,]),'$end':([0,1,5,13,14,15,21,22,23,],[-30,0,-7,-4,-5,-6,-1,-2,-3,]),'SEMI':([2,3,4,10,11,12,16,18,25,26,28,29,30,35,40,42,47,48,49,50,51,],[13,14,15,21,22,23,-19,-8,-28,-17,-25,-26,-27,-18,-22,-10,-20,-21,-23,-24,-29,]),'RMB':([5,13,14,15,19,21,22,23,32,],[-7,-4,-5,-6,-30,-1,-2,-3,42,]),'EQUAL':([7,16,25,28,29,30,33,34,40,44,45,47,48,49,50,51,52,54,56,57,58,],[17,24,-28,-25,-26,-27,46,-16,-22,53,55,-20,-21,-23,-24,-29,-11,-12,-15,-13,-14,]),'LMB':([8,43,],[19,-9,]),'LSB':([9,17,20,24,27,31,36,37,38,39,44,45,46,53,55,],[20,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'MINUS':([17,20,24,25,26,27,28,29,30,31,34,35,36,37,38,39,40,41,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,],[27,27,27,-28,37,27,-25,-26,-27,27,37,37,27,27,27,27,-22,37,27,27,27,-20,-21,-23,-24,-29,37,27,37,27,37,37,37,]),'INT':([17,20,24,27,31,36,37,38,39,44,45,46,53,55,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'FLOAT':([17,20,24,27,31,36,37,38,39,44,45,46,53,55,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'STRING':([17,20,24,27,31,36,37,38,39,44,45,46,53,55,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'PLUS':([25,26,28,29,30,34,35,40,41,47,48,49,50,51,52,54,56,57,58,],[-28,36,-25,-26,-27,36,36,-22,36,-20,-21,-23,-24,-29,36,36,36,36,36,]),'MUL':([25,26,28,29,30,34,35,40,41,47,48,49,50,51,52,54,56,57,58,],[-28,38,-25,-26,-27,38,38,-22,38,38,38,-23,-24,-29,38,38,38,38,38,]),'DIV':([25,26,28,29,30,34,35,40,41,47,48,49,50,51,52,54,56,57,58,],[-28,39,-25,-26,-27,39,39,-22,39,39,39,-23,-24,-29,39,39,39,39,39,]),'RSB':([25,28,29,30,33,34,40,41,47,48,49,50,51,52,54,56,57,58,],[-28,-25,-26,-27,43,-16,-22,51,-20,-21,-23,-24,-29,-11,-12,-15,-13,-14,]),'LB':([25,28,29,30,33,34,40,47,48,49,50,51,52,54,56,57,58,],[-28,-25,-26,-27,44,-16,-22,-20,-21,-23,-24,-29,-11,-12,-15,-13,-14,]),'RB':([25,28,29,30,33,34,40,47,48,49,50,51,52,54,56,57,58,],[-28,-25,-26,-27,45,-16,-22,-20,-21,-23,-24,-29,-11,-12,-15,-13,-14,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,19,],[1,32,]),'variable_declaration':([0,1,19,32,],[2,10,2,10,]),'variable_value_change':([0,1,19,32,],[3,11,3,11,]),'if_statement':([0,1,19,32,],[4,12,4,12,]),'empty':([0,19,],[5,5,]),'if_statement_head':([0,1,19,32,],[8,8,8,8,]),'if_statement_body':([8,],[18,]),'calculate':([17,20,24,27,31,36,37,38,39,44,45,46,53,55,],[26,34,35,40,41,47,48,49,50,52,54,56,57,58,]),'condition':([20,],[33,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression variable_declaration SEMI','expression',3,'p_expression','main.py',131),
  ('expression -> expression variable_value_change SEMI','expression',3,'p_expression','main.py',132),
  ('expression -> expression if_statement SEMI','expression',3,'p_expression','main.py',133),
  ('expression -> variable_declaration SEMI','expression',2,'p_expression_2','main.py',140),
  ('expression -> variable_value_change SEMI','expression',2,'p_expression_2','main.py',141),
  ('expression -> if_statement SEMI','expression',2,'p_expression_2','main.py',142),
  ('expression -> empty','expression',1,'p_expression_empty','main.py',149),
  ('if_statement -> if_statement_head if_statement_body','if_statement',2,'p_if_statement','main.py',158),
  ('if_statement_head -> IF LSB condition RSB','if_statement_head',4,'p_if_statement_head','main.py',165),
  ('if_statement_body -> LMB expression RMB','if_statement_body',3,'p_if_statement_body','main.py',171),
  ('condition -> condition LB calculate','condition',3,'p_condition','main.py',182),
  ('condition -> condition RB calculate','condition',3,'p_condition','main.py',183),
  ('condition -> condition LB EQUAL calculate','condition',4,'p_condition_2','main.py',189),
  ('condition -> condition RB EQUAL calculate','condition',4,'p_condition_2','main.py',190),
  ('condition -> condition EQUAL calculate','condition',3,'p_condition_3','main.py',196),
  ('condition -> calculate','condition',1,'p_condition_4','main.py',202),
  ('variable_value_change -> IDENTIFIER EQUAL calculate','variable_value_change',3,'p_variable_value_change','main.py',209),
  ('variable_declaration -> VAR IDENTIFIER EQUAL calculate','variable_declaration',4,'p_variable_declaration_2','main.py',234),
  ('variable_declaration -> VAR IDENTIFIER','variable_declaration',2,'p_variable_declaration_1','main.py',251),
  ('calculate -> calculate PLUS calculate','calculate',3,'p_add','main.py',280),
  ('calculate -> calculate MINUS calculate','calculate',3,'p_sub','main.py',295),
  ('calculate -> MINUS calculate','calculate',2,'p_calculate2uminus','main.py',299),
  ('calculate -> calculate MUL calculate','calculate',3,'p_mul_div','main.py',304),
  ('calculate -> calculate DIV calculate','calculate',3,'p_mul_div','main.py',305),
  ('calculate -> INT','calculate',1,'p_calculate2num','main.py',316),
  ('calculate -> FLOAT','calculate',1,'p_calculate2num','main.py',317),
  ('calculate -> STRING','calculate',1,'p_calculate2num','main.py',318),
  ('calculate -> IDENTIFIER','calculate',1,'p_calculate2str','main.py',324),
  ('calculate -> LSB calculate RSB','calculate',3,'p_parens','main.py',332),
  ('empty -> <empty>','empty',0,'p_empty','main.py',338),
]
