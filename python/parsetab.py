
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'A ABBR ADDRESS AREA ARTICLE ASIDE AUDIO B BODY COMMA DIV EQUAL HEAD HTML IDENTIFIER LMB LSB OTHER RMB RSBroot : head_expr inside\n    inside : LMB inside_content RMB\n        | LMB root RMB\n    \n    inside_content : attr\n        | empty\n    head_expr : HTML elements_outside\n        | A\n        | ABBR\n        | ADDRESS\n        | AREA\n        | ARTICLE\n        | ASIDE\n        | AUDIO\n        | B\n    \n    elements_outside : LSB elements_inside_comma RSB\n    \n    elements_inside_comma : elements_inside_equal COMMA elements_inside_equal\n    \n    elements_inside_comma : elements_inside_equal\n        | empty\n    \n    elements_inside_equal : attr_root EQUAL attr_root\n    \n    attr_root : attr attr\n    attr_root : attr\n    attr : attr IDENTIFIER\n        | attr OTHER\n    \n    attr : IDENTIFIER\n        | OTHER\n        | HTML\n    empty : '
    
_lr_action_items = {'HTML':([0,13,15,20,21,27,28,34,35,37,38,],[3,22,28,-24,-25,28,-26,28,28,-22,-23,]),'A':([0,13,],[4,4,]),'ABBR':([0,13,],[5,5,]),'ADDRESS':([0,13,],[6,6,]),'AREA':([0,13,],[7,7,]),'ARTICLE':([0,13,],[8,8,]),'ASIDE':([0,13,],[9,9,]),'AUDIO':([0,13,],[10,10,]),'B':([0,13,],[11,11,]),'$end':([1,12,29,30,],[0,-1,-2,-3,]),'LMB':([2,4,5,6,7,8,9,10,11,14,33,],[13,-7,-8,-9,-10,-11,-12,-13,-14,-6,-15,]),'LSB':([3,22,],[15,15,]),'RMB':([12,13,16,17,18,19,20,21,22,29,30,31,32,],[-1,-27,29,30,-4,-5,-24,-25,-26,-2,-3,-22,-23,]),'IDENTIFIER':([13,15,18,20,21,22,27,28,31,32,34,35,36,37,38,],[20,20,31,-24,-25,-26,37,-26,-22,-23,20,20,31,-22,-23,]),'OTHER':([13,15,18,20,21,22,27,28,31,32,34,35,36,37,38,],[21,21,32,-24,-25,-26,38,-26,-22,-23,21,21,32,-22,-23,]),'RSB':([15,20,21,23,24,25,27,28,31,32,36,37,38,39,40,],[-27,-24,-25,33,-17,-18,-21,-26,-22,-23,-20,-22,-23,-16,-19,]),'EQUAL':([20,21,26,27,28,31,32,36,37,38,],[-24,-25,35,-21,-26,-22,-23,-20,-22,-23,]),'COMMA':([20,21,24,27,28,31,32,36,37,38,40,],[-24,-25,34,-21,-26,-22,-23,-20,-22,-23,-19,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'root':([0,13,],[1,17,]),'head_expr':([0,13,],[2,2,]),'inside':([2,],[12,]),'elements_outside':([3,22,],[14,14,]),'inside_content':([13,],[16,]),'attr':([13,15,27,34,35,],[18,27,36,27,27,]),'empty':([13,15,],[19,25,]),'elements_inside_comma':([15,],[23,]),'elements_inside_equal':([15,34,],[24,39,]),'attr_root':([15,34,35,],[26,26,40,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> root","S'",1,None,None,None),
  ('root -> head_expr inside','root',2,'p_root','parser.py',7),
  ('inside -> LMB inside_content RMB','inside',3,'p_inside','parser.py',12),
  ('inside -> LMB root RMB','inside',3,'p_inside','parser.py',13),
  ('inside_content -> attr','inside_content',1,'p_inside_content','parser.py',19),
  ('inside_content -> empty','inside_content',1,'p_inside_content','parser.py',20),
  ('head_expr -> HTML elements_outside','head_expr',2,'p_head','parser.py',25),
  ('head_expr -> A','head_expr',1,'p_head','parser.py',26),
  ('head_expr -> ABBR','head_expr',1,'p_head','parser.py',27),
  ('head_expr -> ADDRESS','head_expr',1,'p_head','parser.py',28),
  ('head_expr -> AREA','head_expr',1,'p_head','parser.py',29),
  ('head_expr -> ARTICLE','head_expr',1,'p_head','parser.py',30),
  ('head_expr -> ASIDE','head_expr',1,'p_head','parser.py',31),
  ('head_expr -> AUDIO','head_expr',1,'p_head','parser.py',32),
  ('head_expr -> B','head_expr',1,'p_head','parser.py',33),
  ('elements_outside -> LSB elements_inside_comma RSB','elements_outside',3,'p_elements_outside','parser.py',39),
  ('elements_inside_comma -> elements_inside_equal COMMA elements_inside_equal','elements_inside_comma',3,'p_elements_inside_comma1','parser.py',45),
  ('elements_inside_comma -> elements_inside_equal','elements_inside_comma',1,'p_elements_inside_comma2','parser.py',51),
  ('elements_inside_comma -> empty','elements_inside_comma',1,'p_elements_inside_comma2','parser.py',52),
  ('elements_inside_equal -> attr_root EQUAL attr_root','elements_inside_equal',3,'p_elements_inside_equal','parser.py',58),
  ('attr_root -> attr attr','attr_root',2,'p_attr0','parser.py',64),
  ('attr_root -> attr','attr_root',1,'p_attr00','parser.py',69),
  ('attr -> attr IDENTIFIER','attr',2,'p_attr1','parser.py',74),
  ('attr -> attr OTHER','attr',2,'p_attr1','parser.py',75),
  ('attr -> IDENTIFIER','attr',1,'p_attr2','parser.py',81),
  ('attr -> OTHER','attr',1,'p_attr2','parser.py',82),
  ('attr -> HTML','attr',1,'p_attr2','parser.py',83),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',89),
]
