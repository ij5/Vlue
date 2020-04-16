
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'A BODY COMMA DIV EQUAL HEAD HTML IDENTIFIER LMB LSB OTHER RMB RSBhead_expr : HTML elements_outside\n    elements_outside : LSB elements_inside_comma RSB\n    \n    elements_inside_comma : elements_inside_equal COMMA elements_inside_equal\n    \n    elements_inside_comma : elements_inside_equal\n        | empty\n    \n    elements_inside_equal : attr_root EQUAL attr_root\n    \n    attr_root : attr attr\n    attr_root : attr\n    attr : attr IDENTIFIER\n        | attr OTHER\n    \n    attr : IDENTIFIER\n        | OTHER\n    empty : '
    
_lr_action_items = {'HTML':([0,],[2,]),'$end':([1,3,12,],[0,-1,-2,]),'LSB':([2,],[4,]),'RSB':([4,5,6,7,9,10,11,15,16,17,18,19,20,21,],[-13,12,-4,-5,-8,-11,-12,-7,-9,-10,-3,-6,-9,-10,]),'IDENTIFIER':([4,9,10,11,13,14,15,16,17,20,21,],[10,16,-11,-12,10,10,20,-9,-10,-9,-10,]),'OTHER':([4,9,10,11,13,14,15,16,17,20,21,],[11,17,-11,-12,11,11,21,-9,-10,-9,-10,]),'COMMA':([6,9,10,11,15,16,17,19,20,21,],[13,-8,-11,-12,-7,-9,-10,-6,-9,-10,]),'EQUAL':([8,9,10,11,15,16,17,20,21,],[14,-8,-11,-12,-7,-9,-10,-9,-10,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'head_expr':([0,],[1,]),'elements_outside':([2,],[3,]),'elements_inside_comma':([4,],[5,]),'elements_inside_equal':([4,13,],[6,18,]),'empty':([4,],[7,]),'attr_root':([4,13,14,],[8,8,19,]),'attr':([4,9,13,14,],[9,15,9,9,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> head_expr","S'",1,None,None,None),
  ('head_expr -> HTML elements_outside','head_expr',2,'p_head','parser.py',7),
  ('elements_outside -> LSB elements_inside_comma RSB','elements_outside',3,'p_elements_outside','parser.py',12),
  ('elements_inside_comma -> elements_inside_equal COMMA elements_inside_equal','elements_inside_comma',3,'p_elements_inside_comma1','parser.py',18),
  ('elements_inside_comma -> elements_inside_equal','elements_inside_comma',1,'p_elements_inside_comma2','parser.py',24),
  ('elements_inside_comma -> empty','elements_inside_comma',1,'p_elements_inside_comma2','parser.py',25),
  ('elements_inside_equal -> attr_root EQUAL attr_root','elements_inside_equal',3,'p_elements_inside_equal','parser.py',31),
  ('attr_root -> attr attr','attr_root',2,'p_attr0','parser.py',37),
  ('attr_root -> attr','attr_root',1,'p_attr00','parser.py',42),
  ('attr -> attr IDENTIFIER','attr',2,'p_attr1','parser.py',47),
  ('attr -> attr OTHER','attr',2,'p_attr1','parser.py',48),
  ('attr -> IDENTIFIER','attr',1,'p_attr2','parser.py',54),
  ('attr -> OTHER','attr',1,'p_attr2','parser.py',55),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',61),
]
