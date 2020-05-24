
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftMULDIVrightUMINUSCATCH CLASS COLON COMMA DEBUG DIV ELSE EQUAL FLOAT FOR FUNCTION GLOBAL IDENTIFIER IF IN INT LB LIST LMB LSB MINUS MUL PLUS PYTHON RB REPEAT RMB RSB SEMI STRING TRY USE VAR WHILE\n    root : expression\n    \n    expression : expression variable_declaration SEMI\n        | expression variable_value_change SEMI\n    \n    expression : expression if_statement\n    \n    expression : expression function\n        | expression function_call SEMI\n    \n    expression : expression repeat\n    \n    expression : expression for\n    \n    expression : expression while\n    \n    expression : expression use SEMI\n    \n    expression : expression error_handling\n    \n    expression : expression variable_alone SEMI\n    \n    expression : expression global_variable SEMI\n    \n    expression : expression class_def\n    \n    expression : expression debug SEMI\n    \n    expression : expression function_class SEMI\n    \n    expression : variable_declaration SEMI\n        | variable_value_change SEMI\n    \n    expression : if_statement\n    \n    expression : function\n        | function_call\n    \n    expression : repeat\n    \n    expression : for\n    \n    expression : while\n    \n    expression : use SEMI\n    \n    expression : error_handling\n    \n    expression : variable_alone SEMI\n    \n    expression : global_variable SEMI\n    \n    expression : class_def\n    \n    expression : debug SEMI\n    \n    expression : function_class SEMI\n    \n    expression : empty\n    \n    error_handling : try catch\n    \n    try : TRY LMB expression RMB\n    \n    catch : CATCH LSB IDENTIFIER RSB LMB expression RMB\n    \n    for : for_head for_body\n    \n    for_head : FOR LSB IDENTIFIER IN IDENTIFIER RSB\n    \n    for_body : LMB expression RMB\n    \n    while : while_head while_body\n    \n    while_head : WHILE LSB condition RSB\n    \n    while_body : LMB expression RMB\n    \n    repeat : repeat_head repeat_body\n    \n    repeat_head : REPEAT LSB calculate RSB\n    \n    repeat_body : LMB expression RMB\n    \n    function_class : VAR IDENTIFIER EQUAL IDENTIFIER LSB parameter RSB\n        | VAR IDENTIFIER EQUAL IDENTIFIER LSB empty RSB\n    \n    function_class : IDENTIFIER EQUAL IDENTIFIER LSB parameter RSB\n        | IDENTIFIER EQUAL IDENTIFIER LSB empty RSB\n    \n    class_def : CLASS IDENTIFIER LMB expression RMB\n    \n    function : function_head function_body\n    \n    function_head : FUNCTION IDENTIFIER LSB parameter RSB\n        | FUNCTION IDENTIFIER LSB empty RSB\n    \n    function_body : LMB expression RMB\n    \n    function_call : IDENTIFIER LSB parameter RSB\n        | IDENTIFIER LSB empty RSB\n    \n    parameter : parameter COMMA calculate\n    \n    parameter : calculate\n    \n    debug : USE DEBUG\n    \n    if_statement : if_statement_1 if_statement_2 if_statement_3\n        | if_statement_1 if_statement_2\n        | if_statement_1 if_statement_3\n        | if_statement_1\n    \n    if_statement_1 : IF LSB condition RSB LMB expression RMB\n    \n    if_statement_2 : ELSE IF LSB condition RSB LMB expression RMB\n    \n    if_statement_2 : if_statement_2 ELSE IF LSB condition RSB LMB expression RMB\n    \n    if_statement_3 : ELSE LMB expression RMB\n    \n    condition : condition LB calculate\n        | condition RB calculate\n    \n    condition : condition LB EQUAL calculate\n        | condition RB EQUAL calculate\n    \n    condition : condition EQUAL calculate\n    \n    condition : calculate\n    \n    use : USE use_params\n    \n    use_params : IDENTIFIER\n    \n    global_variable : GLOBAL IDENTIFIER\n    \n    variable_alone : IDENTIFIER\n    \n    variable_value_change : IDENTIFIER EQUAL LIST\n    \n    variable_value_change : IDENTIFIER EQUAL calculate\n    \n    variable_declaration : VAR IDENTIFIER LIST EQUAL calculate\n    \n    variable_declaration : VAR IDENTIFIER EQUAL calculate\n    \n    variable_declaration : VAR IDENTIFIER\n    calculate : calculate PLUS calculatecalculate : calculate MINUS calculatecalculate : MINUS calculate %prec UMINUS\n    calculate : calculate MUL calculate\n        | calculate DIV calculate\n    \n    calculate : INT\n        | FLOAT\n        | STRING\n    \n    calculate : IDENTIFIER\n    \n    calculate : IDENTIFIER LIST\n    \n    calculate : LIST\n    calculate : LSB calculate RSBempty : '
    
_lr_action_items = {'VAR':([0,2,5,6,7,8,9,10,12,15,18,21,38,39,41,42,43,45,48,51,52,53,54,55,56,57,61,62,64,65,66,67,68,69,70,71,75,84,85,86,87,88,89,90,91,92,108,111,112,113,114,115,117,124,136,138,141,142,143,144,145,147,170,172,173,188,189,196,197,198,199,200,201,202,203,204,],[19,19,-19,-20,-21,-22,-23,-24,-26,-29,-32,-62,-4,-5,-7,-8,-9,-11,-14,-17,-18,-25,-27,-28,-30,-31,-60,-61,-50,19,-42,19,-36,19,-39,19,-33,19,-2,-3,-6,-10,-12,-13,-15,-16,-59,19,19,19,19,19,19,19,-54,-55,19,-53,-44,-38,-41,19,-66,-49,19,19,19,19,19,-63,19,19,-35,19,-64,-65,]),'IDENTIFIER':([0,2,5,6,7,8,9,10,12,15,18,19,21,26,28,29,31,38,39,41,42,43,45,48,51,52,53,54,55,56,57,59,60,61,62,64,65,66,67,68,69,70,71,75,79,81,82,83,84,85,86,87,88,89,90,91,92,94,98,99,108,111,112,113,114,115,116,117,120,124,125,128,130,131,132,133,136,137,138,140,141,142,143,144,145,147,149,150,151,155,159,168,170,172,173,175,177,188,189,196,197,198,199,200,201,202,203,204,],[20,20,-19,-20,-21,-22,-23,-24,-26,-29,-32,58,-62,74,77,78,80,-4,-5,-7,-8,-9,-11,-14,-17,-18,-25,-27,-28,-30,-31,95,103,-60,-61,-50,20,-42,20,-36,20,-39,20,-33,103,103,122,103,20,-2,-3,-6,-10,-12,-13,-15,-16,126,103,103,-59,20,20,20,20,20,146,20,103,20,103,103,103,103,103,103,-54,103,-55,103,20,-53,-44,-38,-41,20,103,103,103,181,103,103,-66,-49,20,103,103,20,20,20,20,-63,20,20,-35,20,-64,-65,]),'USE':([0,2,5,6,7,8,9,10,12,15,18,21,38,39,41,42,43,45,48,51,52,53,54,55,56,57,61,62,64,65,66,67,68,69,70,71,75,84,85,86,87,88,89,90,91,92,108,111,112,113,114,115,117,124,136,138,141,142,143,144,145,147,170,172,173,188,189,196,197,198,199,200,201,202,203,204,],[26,26,-19,-20,-21,-22,-23,-24,-26,-29,-32,-62,-4,-5,-7,-8,-9,-11,-14,-17,-18,-25,-27,-28,-30,-31,-60,-61,-50,26,-42,26,-36,26,-39,26,-33,26,-2,-3,-6,-10,-12,-13,-15,-16,-59,26,26,26,26,26,26,26,-54,-55,26,-53,-44,-38,-41,26,-66,-49,26,26,26,26,26,-63,26,26,-35,26,-64,-65,]),'GLOBAL':([0,2,5,6,7,8,9,10,12,15,18,21,38,39,41,42,43,45,48,51,52,53,54,55,56,57,61,62,64,65,66,67,68,69,70,71,75,84,85,86,87,88,89,90,91,92,108,111,112,113,114,115,117,124,136,138,141,142,143,144,145,147,170,172,173,188,189,196,197,198,199,200,201,202,203,204,],[28,28,-19,-20,-21,-22,-23,-24,-26,-29,-32,-62,-4,-5,-7,-8,-9,-11,-14,-17,-18,-25,-27,-28,-30,-31,-60,-61,-50,28,-42,28,-36,28,-39,28,-33,28,-2,-3,-6,-10,-12,-13,-15,-16,-59,28,28,28,28,28,28,28,-54,-55,28,-53,-44,-38,-41,28,-66,-49,28,28,28,28,28,-63,28,28,-35,28,-64,-65,]),'CLASS':([0,2,5,6,7,8,9,10,12,15,18,21,38,39,41,42,43,45,48,51,52,53,54,55,56,57,61,62,64,65,66,67,68,69,70,71,75,84,85,86,87,88,89,90,91,92,108,111,112,113,114,115,117,124,136,138,141,142,143,144,145,147,170,172,173,188,189,196,197,198,199,200,201,202,203,204,],[29,29,-19,-20,-21,-22,-23,-24,-26,-29,-32,-62,-4,-5,-7,-8,-9,-11,-14,-17,-18,-25,-27,-28,-30,-31,-60,-61,-50,29,-42,29,-36,29,-39,29,-33,29,-2,-3,-6,-10,-12,-13,-15,-16,-59,29,29,29,29,29,29,29,-54,-55,29,-53,-44,-38,-41,29,-66,-49,29,29,29,29,29,-63,29,29,-35,29,-64,-65,]),'IF':([0,2,5,6,7,8,9,10,12,15,18,21,38,39,41,42,43,45,48,51,52,53,54,55,56,57,61,62,63,64,65,66,67,68,69,70,71,75,84,85,86,87,88,89,90,91,92,108,109,111,112,113,114,115,117,124,136,138,141,142,143,144,145,147,170,172,173,188,189,196,197,198,199,200,201,202,203,204,],[30,30,-19,-20,-21,-22,-23,-24,-26,-29,-32,-62,-4,-5,-7,-8,-9,-11,-14,-17,-18,-25,-27,-28,-30,-31,-60,-61,110,-50,30,-42,30,-36,30,-39,30,-33,30,-2,-3,-6,-10,-12,-13,-15,-16,-59,139,30,30,30,30,30,30,30,-54,-55,30,-53,-44,-38,-41,30,-66,-49,30,30,30,30,30,-63,30,30,-35,30,-64,-65,]),'FUNCTION':([0,2,5,6,7,8,9,10,12,15,18,21,38,39,41,42,43,45,48,51,52,53,54,55,56,57,61,62,64,65,66,67,68,69,70,71,75,84,85,86,87,88,89,90,91,92,108,111,112,113,114,115,117,124,136,138,141,142,143,144,145,147,170,172,173,188,189,196,197,198,199,200,201,202,203,204,],[31,31,-19,-20,-21,-22,-23,-24,-26,-29,-32,-62,-4,-5,-7,-8,-9,-11,-14,-17,-18,-25,-27,-28,-30,-31,-60,-61,-50,31,-42,31,-36,31,-39,31,-33,31,-2,-3,-6,-10,-12,-13,-15,-16,-59,31,31,31,31,31,31,31,-54,-55,31,-53,-44,-38,-41,31,-66,-49,31,31,31,31,31,-63,31,31,-35,31,-64,-65,]),'REPEAT':([0,2,5,6,7,8,9,10,12,15,18,21,38,39,41,42,43,45,48,51,52,53,54,55,56,57,61,62,64,65,66,67,68,69,70,71,75,84,85,86,87,88,89,90,91,92,108,111,112,113,114,115,117,124,136,138,141,142,143,144,145,147,170,172,173,188,189,196,197,198,199,200,201,202,203,204,],[32,32,-19,-20,-21,-22,-23,-24,-26,-29,-32,-62,-4,-5,-7,-8,-9,-11,-14,-17,-18,-25,-27,-28,-30,-31,-60,-61,-50,32,-42,32,-36,32,-39,32,-33,32,-2,-3,-6,-10,-12,-13,-15,-16,-59,32,32,32,32,32,32,32,-54,-55,32,-53,-44,-38,-41,32,-66,-49,32,32,32,32,32,-63,32,32,-35,32,-64,-65,]),'FOR':([0,2,5,6,7,8,9,10,12,15,18,21,38,39,41,42,43,45,48,51,52,53,54,55,56,57,61,62,64,65,66,67,68,69,70,71,75,84,85,86,87,88,89,90,91,92,108,111,112,113,114,115,117,124,136,138,141,142,143,144,145,147,170,172,173,188,189,196,197,198,199,200,201,202,203,204,],[33,33,-19,-20,-21,-22,-23,-24,-26,-29,-32,-62,-4,-5,-7,-8,-9,-11,-14,-17,-18,-25,-27,-28,-30,-31,-60,-61,-50,33,-42,33,-36,33,-39,33,-33,33,-2,-3,-6,-10,-12,-13,-15,-16,-59,33,33,33,33,33,33,33,-54,-55,33,-53,-44,-38,-41,33,-66,-49,33,33,33,33,33,-63,33,33,-35,33,-64,-65,]),'WHILE':([0,2,5,6,7,8,9,10,12,15,18,21,38,39,41,42,43,45,48,51,52,53,54,55,56,57,61,62,64,65,66,67,68,69,70,71,75,84,85,86,87,88,89,90,91,92,108,111,112,113,114,115,117,124,136,138,141,142,143,144,145,147,170,172,173,188,189,196,197,198,199,200,201,202,203,204,],[34,34,-19,-20,-21,-22,-23,-24,-26,-29,-32,-62,-4,-5,-7,-8,-9,-11,-14,-17,-18,-25,-27,-28,-30,-31,-60,-61,-50,34,-42,34,-36,34,-39,34,-33,34,-2,-3,-6,-10,-12,-13,-15,-16,-59,34,34,34,34,34,34,34,-54,-55,34,-53,-44,-38,-41,34,-66,-49,34,34,34,34,34,-63,34,34,-35,34,-64,-65,]),'TRY':([0,2,5,6,7,8,9,10,12,15,18,21,38,39,41,42,43,45,48,51,52,53,54,55,56,57,61,62,64,65,66,67,68,69,70,71,75,84,85,86,87,88,89,90,91,92,108,111,112,113,114,115,117,124,136,138,141,142,143,144,145,147,170,172,173,188,189,196,197,198,199,200,201,202,203,204,],[35,35,-19,-20,-21,-22,-23,-24,-26,-29,-32,-62,-4,-5,-7,-8,-9,-11,-14,-17,-18,-25,-27,-28,-30,-31,-60,-61,-50,35,-42,35,-36,35,-39,35,-33,35,-2,-3,-6,-10,-12,-13,-15,-16,-59,35,35,35,35,35,35,35,-54,-55,35,-53,-44,-38,-41,35,-66,-49,35,35,35,35,35,-63,35,35,-35,35,-64,-65,]),'$end':([0,1,2,5,6,7,8,9,10,12,15,18,21,38,39,41,42,43,45,48,51,52,53,54,55,56,57,61,62,64,66,68,70,75,85,86,87,88,89,90,91,92,108,136,138,142,143,144,145,170,172,198,201,203,204,],[-94,0,-1,-19,-20,-21,-22,-23,-24,-26,-29,-32,-62,-4,-5,-7,-8,-9,-11,-14,-17,-18,-25,-27,-28,-30,-31,-60,-61,-50,-42,-36,-39,-33,-2,-3,-6,-10,-12,-13,-15,-16,-59,-54,-55,-53,-44,-38,-41,-66,-49,-63,-35,-64,-65,]),'SEMI':([3,4,11,13,14,16,17,20,36,37,40,44,46,47,49,50,58,72,73,74,77,95,96,97,100,101,102,103,107,126,127,129,135,136,138,158,162,163,164,165,166,184,185,193,194,],[51,52,53,54,55,56,57,-76,85,86,87,88,89,90,91,92,-81,-73,-58,-74,-75,-90,-77,-78,-87,-88,-89,-90,-92,-90,-80,-91,-84,-54,-55,-79,-82,-83,-85,-86,-93,-47,-48,-45,-46,]),'RMB':([5,6,7,8,9,10,12,15,18,21,38,39,41,42,43,45,48,51,52,53,54,55,56,57,61,62,64,65,66,67,68,69,70,71,75,84,85,86,87,88,89,90,91,92,108,111,112,113,114,115,117,124,136,138,141,142,143,144,145,147,170,172,173,188,189,196,197,198,199,200,201,202,203,204,],[-19,-20,-21,-22,-23,-24,-26,-29,-32,-62,-4,-5,-7,-8,-9,-11,-14,-17,-18,-25,-27,-28,-30,-31,-60,-61,-50,-94,-42,-94,-36,-94,-39,-94,-33,-94,-2,-3,-6,-10,-12,-13,-15,-16,-59,-94,142,143,144,145,-94,157,-54,-55,170,-53,-44,-38,-41,172,-66,-49,-94,-94,198,-94,201,-63,-94,203,-35,204,-64,-65,]),'EQUAL':([20,58,93,100,101,102,103,107,118,119,123,129,135,149,150,162,163,164,165,166,169,174,176,178,186,190,191,],[59,94,125,-87,-88,-89,-90,-92,151,-72,151,-91,-84,175,177,-82,-83,-85,-86,-93,151,-67,-68,-71,151,-69,-70,]),'LSB':([20,30,32,33,34,59,60,76,79,80,81,83,94,95,98,99,110,120,125,126,128,130,131,132,133,137,139,140,149,150,151,159,168,175,177,],[60,79,81,82,83,98,98,116,98,120,98,98,98,128,98,98,140,98,98,159,98,98,98,98,98,98,168,98,98,98,98,98,98,98,98,]),'ELSE':([21,61,198,203,204,],[63,109,-63,-64,-65,]),'LMB':([22,23,24,25,35,63,78,109,148,154,156,171,179,180,187,192,195,],[65,67,69,71,84,111,117,111,173,-43,-40,188,-51,-52,196,-37,199,]),'DEBUG':([26,],[73,]),'CATCH':([27,157,],[76,-34,]),'LIST':([58,59,60,79,81,83,94,95,98,99,103,120,125,126,128,130,131,132,133,137,140,149,150,151,159,168,175,177,],[93,96,107,107,107,107,107,129,107,107,129,107,107,129,107,107,107,107,107,107,107,107,107,107,107,107,107,107,]),'MINUS':([59,60,79,81,83,94,95,96,97,98,99,100,101,102,103,106,107,119,120,121,125,126,127,128,129,130,131,132,133,134,135,137,140,149,150,151,158,159,162,163,164,165,166,167,168,174,175,176,177,178,190,191,],[99,99,99,99,99,99,-90,-92,131,99,99,-87,-88,-89,-90,131,-92,131,99,131,99,-90,131,99,-91,99,99,99,99,131,-84,99,99,99,99,99,131,99,-82,-83,-85,-86,-93,131,99,131,99,131,99,131,131,131,]),'INT':([59,60,79,81,83,94,98,99,120,125,128,130,131,132,133,137,140,149,150,151,159,168,175,177,],[100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,]),'FLOAT':([59,60,79,81,83,94,98,99,120,125,128,130,131,132,133,137,140,149,150,151,159,168,175,177,],[101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,]),'STRING':([59,60,79,81,83,94,98,99,120,125,128,130,131,132,133,137,140,149,150,151,159,168,175,177,],[102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,]),'RSB':([60,100,101,102,103,104,105,106,107,118,119,120,121,123,128,129,134,135,146,152,153,159,160,161,162,163,164,165,166,167,169,174,176,178,181,182,183,186,190,191,],[-94,-87,-88,-89,-90,136,138,-57,-92,148,-72,-94,154,156,-94,-91,166,-84,171,179,180,-94,184,185,-82,-83,-85,-86,-93,-56,187,-67,-68,-71,192,193,194,195,-69,-70,]),'PLUS':([95,96,97,100,101,102,103,106,107,119,121,126,127,129,134,135,158,162,163,164,165,166,167,174,176,178,190,191,],[-90,-92,130,-87,-88,-89,-90,130,-92,130,130,-90,130,-91,130,-84,130,-82,-83,-85,-86,-93,130,130,130,130,130,130,]),'MUL':([95,96,97,100,101,102,103,106,107,119,121,126,127,129,134,135,158,162,163,164,165,166,167,174,176,178,190,191,],[-90,-92,132,-87,-88,-89,-90,132,-92,132,132,-90,132,-91,132,-84,132,132,132,-85,-86,-93,132,132,132,132,132,132,]),'DIV':([95,96,97,100,101,102,103,106,107,119,121,126,127,129,134,135,158,162,163,164,165,166,167,174,176,178,190,191,],[-90,-92,133,-87,-88,-89,-90,133,-92,133,133,-90,133,-91,133,-84,133,133,133,-85,-86,-93,133,133,133,133,133,133,]),'COMMA':([100,101,102,103,104,106,107,129,135,152,160,162,163,164,165,166,167,182,],[-87,-88,-89,-90,137,-57,-92,-91,-84,137,137,-82,-83,-85,-86,-93,-56,137,]),'LB':([100,101,102,103,107,118,119,123,129,135,162,163,164,165,166,169,174,176,178,186,190,191,],[-87,-88,-89,-90,-92,149,-72,149,-91,-84,-82,-83,-85,-86,-93,149,-67,-68,-71,149,-69,-70,]),'RB':([100,101,102,103,107,118,119,123,129,135,162,163,164,165,166,169,174,176,178,186,190,191,],[-87,-88,-89,-90,-92,150,-72,150,-91,-84,-82,-83,-85,-86,-93,150,-67,-68,-71,150,-69,-70,]),'IN':([122,],[155,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'root':([0,],[1,]),'expression':([0,65,67,69,71,84,111,117,173,188,196,199,],[2,112,113,114,115,124,141,147,189,197,200,202,]),'variable_declaration':([0,2,65,67,69,71,84,111,112,113,114,115,117,124,141,147,173,188,189,196,197,199,200,202,],[3,36,3,3,3,3,3,3,36,36,36,36,3,36,36,36,3,3,36,3,36,3,36,36,]),'variable_value_change':([0,2,65,67,69,71,84,111,112,113,114,115,117,124,141,147,173,188,189,196,197,199,200,202,],[4,37,4,4,4,4,4,4,37,37,37,37,4,37,37,37,4,4,37,4,37,4,37,37,]),'if_statement':([0,2,65,67,69,71,84,111,112,113,114,115,117,124,141,147,173,188,189,196,197,199,200,202,],[5,38,5,5,5,5,5,5,38,38,38,38,5,38,38,38,5,5,38,5,38,5,38,38,]),'function':([0,2,65,67,69,71,84,111,112,113,114,115,117,124,141,147,173,188,189,196,197,199,200,202,],[6,39,6,6,6,6,6,6,39,39,39,39,6,39,39,39,6,6,39,6,39,6,39,39,]),'function_call':([0,2,65,67,69,71,84,111,112,113,114,115,117,124,141,147,173,188,189,196,197,199,200,202,],[7,40,7,7,7,7,7,7,40,40,40,40,7,40,40,40,7,7,40,7,40,7,40,40,]),'repeat':([0,2,65,67,69,71,84,111,112,113,114,115,117,124,141,147,173,188,189,196,197,199,200,202,],[8,41,8,8,8,8,8,8,41,41,41,41,8,41,41,41,8,8,41,8,41,8,41,41,]),'for':([0,2,65,67,69,71,84,111,112,113,114,115,117,124,141,147,173,188,189,196,197,199,200,202,],[9,42,9,9,9,9,9,9,42,42,42,42,9,42,42,42,9,9,42,9,42,9,42,42,]),'while':([0,2,65,67,69,71,84,111,112,113,114,115,117,124,141,147,173,188,189,196,197,199,200,202,],[10,43,10,10,10,10,10,10,43,43,43,43,10,43,43,43,10,10,43,10,43,10,43,43,]),'use':([0,2,65,67,69,71,84,111,112,113,114,115,117,124,141,147,173,188,189,196,197,199,200,202,],[11,44,11,11,11,11,11,11,44,44,44,44,11,44,44,44,11,11,44,11,44,11,44,44,]),'error_handling':([0,2,65,67,69,71,84,111,112,113,114,115,117,124,141,147,173,188,189,196,197,199,200,202,],[12,45,12,12,12,12,12,12,45,45,45,45,12,45,45,45,12,12,45,12,45,12,45,45,]),'variable_alone':([0,2,65,67,69,71,84,111,112,113,114,115,117,124,141,147,173,188,189,196,197,199,200,202,],[13,46,13,13,13,13,13,13,46,46,46,46,13,46,46,46,13,13,46,13,46,13,46,46,]),'global_variable':([0,2,65,67,69,71,84,111,112,113,114,115,117,124,141,147,173,188,189,196,197,199,200,202,],[14,47,14,14,14,14,14,14,47,47,47,47,14,47,47,47,14,14,47,14,47,14,47,47,]),'class_def':([0,2,65,67,69,71,84,111,112,113,114,115,117,124,141,147,173,188,189,196,197,199,200,202,],[15,48,15,15,15,15,15,15,48,48,48,48,15,48,48,48,15,15,48,15,48,15,48,48,]),'debug':([0,2,65,67,69,71,84,111,112,113,114,115,117,124,141,147,173,188,189,196,197,199,200,202,],[16,49,16,16,16,16,16,16,49,49,49,49,16,49,49,49,16,16,49,16,49,16,49,49,]),'function_class':([0,2,65,67,69,71,84,111,112,113,114,115,117,124,141,147,173,188,189,196,197,199,200,202,],[17,50,17,17,17,17,17,17,50,50,50,50,17,50,50,50,17,17,50,17,50,17,50,50,]),'empty':([0,60,65,67,69,71,84,111,117,120,128,159,173,188,196,199,],[18,105,18,18,18,18,18,18,18,153,161,183,18,18,18,18,]),'if_statement_1':([0,2,65,67,69,71,84,111,112,113,114,115,117,124,141,147,173,188,189,196,197,199,200,202,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'function_head':([0,2,65,67,69,71,84,111,112,113,114,115,117,124,141,147,173,188,189,196,197,199,200,202,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'repeat_head':([0,2,65,67,69,71,84,111,112,113,114,115,117,124,141,147,173,188,189,196,197,199,200,202,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'for_head':([0,2,65,67,69,71,84,111,112,113,114,115,117,124,141,147,173,188,189,196,197,199,200,202,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'while_head':([0,2,65,67,69,71,84,111,112,113,114,115,117,124,141,147,173,188,189,196,197,199,200,202,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'try':([0,2,65,67,69,71,84,111,112,113,114,115,117,124,141,147,173,188,189,196,197,199,200,202,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'if_statement_2':([21,],[61,]),'if_statement_3':([21,61,],[62,108,]),'function_body':([22,],[64,]),'repeat_body':([23,],[66,]),'for_body':([24,],[68,]),'while_body':([25,],[70,]),'use_params':([26,],[72,]),'catch':([27,],[75,]),'calculate':([59,60,79,81,83,94,98,99,120,125,128,130,131,132,133,137,140,149,150,151,159,168,175,177,],[97,106,119,121,119,127,134,135,106,158,106,162,163,164,165,167,119,174,176,178,106,119,190,191,]),'parameter':([60,120,128,159,],[104,152,160,182,]),'condition':([79,83,140,168,],[118,123,169,186,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> root","S'",1,None,None,None),
  ('root -> expression','root',1,'p_root','main.py',155),
  ('expression -> expression variable_declaration SEMI','expression',3,'p_expression_variable','main.py',169),
  ('expression -> expression variable_value_change SEMI','expression',3,'p_expression_variable','main.py',170),
  ('expression -> expression if_statement','expression',2,'p_expression_if_statement','main.py',187),
  ('expression -> expression function','expression',2,'p_expression_function','main.py',198),
  ('expression -> expression function_call SEMI','expression',3,'p_expression_function','main.py',199),
  ('expression -> expression repeat','expression',2,'p_expression_repeat','main.py',205),
  ('expression -> expression for','expression',2,'p_expression_for','main.py',211),
  ('expression -> expression while','expression',2,'p_expression_while','main.py',217),
  ('expression -> expression use SEMI','expression',3,'p_expression_use','main.py',223),
  ('expression -> expression error_handling','expression',2,'p_expression_error_handling','main.py',229),
  ('expression -> expression variable_alone SEMI','expression',3,'p_expression_variable_alone','main.py',235),
  ('expression -> expression global_variable SEMI','expression',3,'p_expression_global_variable','main.py',241),
  ('expression -> expression class_def','expression',2,'p_expression_class_def','main.py',247),
  ('expression -> expression debug SEMI','expression',3,'p_expression_debug','main.py',253),
  ('expression -> expression function_class SEMI','expression',3,'p_expression_function_class','main.py',259),
  ('expression -> variable_declaration SEMI','expression',2,'p_expression_variable_2','main.py',267),
  ('expression -> variable_value_change SEMI','expression',2,'p_expression_variable_2','main.py',268),
  ('expression -> if_statement','expression',1,'p_expression_if_statement_2','main.py',279),
  ('expression -> function','expression',1,'p_expression_function_2','main.py',287),
  ('expression -> function_call','expression',1,'p_expression_function_2','main.py',288),
  ('expression -> repeat','expression',1,'p_expression_repeat_2','main.py',294),
  ('expression -> for','expression',1,'p_expression_for_2','main.py',300),
  ('expression -> while','expression',1,'p_expression_while_2','main.py',306),
  ('expression -> use SEMI','expression',2,'p_expression_use_2','main.py',312),
  ('expression -> error_handling','expression',1,'p_expression_error_handling_2','main.py',318),
  ('expression -> variable_alone SEMI','expression',2,'p_expression_variable_alone_2','main.py',324),
  ('expression -> global_variable SEMI','expression',2,'p_expression_global_variable_2','main.py',330),
  ('expression -> class_def','expression',1,'p_expression_class_def_2','main.py',336),
  ('expression -> debug SEMI','expression',2,'p_expression_debug_2','main.py',342),
  ('expression -> function_class SEMI','expression',2,'p_expression_function_class_2','main.py',348),
  ('expression -> empty','expression',1,'p_expression_empty','main.py',356),
  ('error_handling -> try catch','error_handling',2,'p_error_handling','main.py',365),
  ('try -> TRY LMB expression RMB','try',4,'p_try','main.py',371),
  ('catch -> CATCH LSB IDENTIFIER RSB LMB expression RMB','catch',7,'p_catch','main.py',382),
  ('for -> for_head for_body','for',2,'p_for','main.py',395),
  ('for_head -> FOR LSB IDENTIFIER IN IDENTIFIER RSB','for_head',6,'p_for_head','main.py',403),
  ('for_body -> LMB expression RMB','for_body',3,'p_for_body','main.py',409),
  ('while -> while_head while_body','while',2,'p_while','main.py',420),
  ('while_head -> WHILE LSB condition RSB','while_head',4,'p_while_head','main.py',428),
  ('while_body -> LMB expression RMB','while_body',3,'p_while_body','main.py',434),
  ('repeat -> repeat_head repeat_body','repeat',2,'p_repeat','main.py',446),
  ('repeat_head -> REPEAT LSB calculate RSB','repeat_head',4,'p_repeat_head','main.py',454),
  ('repeat_body -> LMB expression RMB','repeat_body',3,'p_repeat_body','main.py',460),
  ('function_class -> VAR IDENTIFIER EQUAL IDENTIFIER LSB parameter RSB','function_class',7,'p_function_class_declaration','main.py',471),
  ('function_class -> VAR IDENTIFIER EQUAL IDENTIFIER LSB empty RSB','function_class',7,'p_function_class_declaration','main.py',472),
  ('function_class -> IDENTIFIER EQUAL IDENTIFIER LSB parameter RSB','function_class',6,'p_function_class_call','main.py',481),
  ('function_class -> IDENTIFIER EQUAL IDENTIFIER LSB empty RSB','function_class',6,'p_function_class_call','main.py',482),
  ('class_def -> CLASS IDENTIFIER LMB expression RMB','class_def',5,'p_class_def','main.py',493),
  ('function -> function_head function_body','function',2,'p_function','main.py',508),
  ('function_head -> FUNCTION IDENTIFIER LSB parameter RSB','function_head',5,'p_function_head','main.py',516),
  ('function_head -> FUNCTION IDENTIFIER LSB empty RSB','function_head',5,'p_function_head','main.py',517),
  ('function_body -> LMB expression RMB','function_body',3,'p_function_body','main.py',526),
  ('function_call -> IDENTIFIER LSB parameter RSB','function_call',4,'p_function_call','main.py',537),
  ('function_call -> IDENTIFIER LSB empty RSB','function_call',4,'p_function_call','main.py',538),
  ('parameter -> parameter COMMA calculate','parameter',3,'p_parameter','main.py',549),
  ('parameter -> calculate','parameter',1,'p_parameter_2','main.py',555),
  ('debug -> USE DEBUG','debug',2,'p_debug','main.py',567),
  ('if_statement -> if_statement_1 if_statement_2 if_statement_3','if_statement',3,'p_if_statement','main.py',577),
  ('if_statement -> if_statement_1 if_statement_2','if_statement',2,'p_if_statement','main.py',578),
  ('if_statement -> if_statement_1 if_statement_3','if_statement',2,'p_if_statement','main.py',579),
  ('if_statement -> if_statement_1','if_statement',1,'p_if_statement','main.py',580),
  ('if_statement_1 -> IF LSB condition RSB LMB expression RMB','if_statement_1',7,'p_if_statement_1','main.py',592),
  ('if_statement_2 -> ELSE IF LSB condition RSB LMB expression RMB','if_statement_2',8,'p_if_statement_2','main.py',601),
  ('if_statement_2 -> if_statement_2 ELSE IF LSB condition RSB LMB expression RMB','if_statement_2',9,'p_if_statement_2_2','main.py',612),
  ('if_statement_3 -> ELSE LMB expression RMB','if_statement_3',4,'p_if_statement_3','main.py',623),
  ('condition -> condition LB calculate','condition',3,'p_condition','main.py',636),
  ('condition -> condition RB calculate','condition',3,'p_condition','main.py',637),
  ('condition -> condition LB EQUAL calculate','condition',4,'p_condition_2','main.py',643),
  ('condition -> condition RB EQUAL calculate','condition',4,'p_condition_2','main.py',644),
  ('condition -> condition EQUAL calculate','condition',3,'p_condition_3','main.py',650),
  ('condition -> calculate','condition',1,'p_condition_4','main.py',656),
  ('use -> USE use_params','use',2,'p_use','main.py',666),
  ('use_params -> IDENTIFIER','use_params',1,'p_use_params','main.py',687),
  ('global_variable -> GLOBAL IDENTIFIER','global_variable',2,'p_global_variable','main.py',694),
  ('variable_alone -> IDENTIFIER','variable_alone',1,'p_variable_alone','main.py',702),
  ('variable_value_change -> IDENTIFIER EQUAL LIST','variable_value_change',3,'p_variable_value_change_list','main.py',710),
  ('variable_value_change -> IDENTIFIER EQUAL calculate','variable_value_change',3,'p_variable_value_change','main.py',716),
  ('variable_declaration -> VAR IDENTIFIER LIST EQUAL calculate','variable_declaration',5,'p_variable_declaration_list','main.py',744),
  ('variable_declaration -> VAR IDENTIFIER EQUAL calculate','variable_declaration',4,'p_variable_declaration_2','main.py',750),
  ('variable_declaration -> VAR IDENTIFIER','variable_declaration',2,'p_variable_declaration_1','main.py',766),
  ('calculate -> calculate PLUS calculate','calculate',3,'p_add','main.py',795),
  ('calculate -> calculate MINUS calculate','calculate',3,'p_sub','main.py',831),
  ('calculate -> MINUS calculate','calculate',2,'p_calculate2uminus','main.py',835),
  ('calculate -> calculate MUL calculate','calculate',3,'p_mul_div','main.py',840),
  ('calculate -> calculate DIV calculate','calculate',3,'p_mul_div','main.py',841),
  ('calculate -> INT','calculate',1,'p_calculate2num','main.py',852),
  ('calculate -> FLOAT','calculate',1,'p_calculate2num','main.py',853),
  ('calculate -> STRING','calculate',1,'p_calculate2num','main.py',854),
  ('calculate -> IDENTIFIER','calculate',1,'p_calculate2str','main.py',860),
  ('calculate -> IDENTIFIER LIST','calculate',2,'p_calculate2list','main.py',869),
  ('calculate -> LIST','calculate',1,'p_calculate2list_2','main.py',875),
  ('calculate -> LSB calculate RSB','calculate',3,'p_parens','main.py',880),
  ('empty -> <empty>','empty',0,'p_empty','main.py',886),
]
