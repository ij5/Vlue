
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'IF INT LB LMB LSB RB RMB RSB\n    statement : expression\n        | if_statement\n    \n    if_statement : IF LSB expression RSB LMB statement RMB\n    \n    expression : condition\n        | empty\n    \n    condition : INT operator INT\n    \n    operator : LB\n        | RB\n    \n    empty : \n    '
    
_lr_action_items = {'IF':([0,15,],[6,6,]),'INT':([0,8,9,10,11,15,],[7,7,13,-7,-8,7,]),'$end':([0,1,2,3,4,5,13,17,],[-9,0,-1,-2,-4,-5,-6,-3,]),'RMB':([2,3,4,5,13,15,16,17,],[-1,-2,-4,-5,-6,-9,17,-3,]),'RSB':([4,5,8,12,13,],[-4,-5,-9,14,-6,]),'LSB':([6,],[8,]),'LB':([7,],[10,]),'RB':([7,],[11,]),'LMB':([14,],[15,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,15,],[1,16,]),'expression':([0,8,15,],[2,12,2,]),'if_statement':([0,15,],[3,3,]),'condition':([0,8,15,],[4,4,4,]),'empty':([0,8,15,],[5,5,5,]),'operator':([7,],[9,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> expression','statement',1,'p_statement','parser.py',7),
  ('statement -> if_statement','statement',1,'p_statement','parser.py',8),
  ('if_statement -> IF LSB expression RSB LMB statement RMB','if_statement',7,'p_if_statement','parser.py',14),
  ('expression -> condition','expression',1,'p_expression','parser.py',19),
  ('expression -> empty','expression',1,'p_expression','parser.py',20),
  ('condition -> INT operator INT','condition',3,'p_condition','parser.py',25),
  ('operator -> LB','operator',1,'p_operator','parser.py',30),
  ('operator -> RB','operator',1,'p_operator','parser.py',31),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',36),
]
