
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftMULDIVrightUMINUSCATCH CLASS COLON COMMA DEBUG DIV DOT ELSE EQUAL FLOAT FOR FUNCTION GLOBAL IDENTIFIER IF IN INT LB LIST LMB LSB MINUS MUL PLUS PYTHON RB REPEAT RMB RSB SEMI STRING TRY USE VAR WHILE\n    root : expression\n    \n    expression : expression variable_declaration SEMI\n        | expression variable_value_change SEMI\n    \n    expression : expression if_statement\n    \n    expression : expression function\n    \n    expression : expression repeat\n    \n    expression : expression for\n    \n    expression : expression while\n    \n    expression : expression use SEMI\n    \n    expression : expression error_handling\n    \n    expression : expression variable_alone SEMI\n    \n    expression : expression global_variable SEMI\n    \n    expression : expression class_def\n    \n    expression : expression debug SEMI\n    \n    expression : expression function_class SEMI\n    \n    expression : expression inside SEMI\n    \n    expression : variable_declaration SEMI\n        | variable_value_change SEMI\n    \n    expression : if_statement\n    \n    expression : function\n    \n    expression : repeat\n    \n    expression : for\n    \n    expression : while\n    \n    expression : use SEMI\n    \n    expression : error_handling\n    \n    expression : variable_alone SEMI\n    \n    expression : global_variable SEMI\n    \n    expression : class_def\n    \n    expression : debug SEMI\n    \n    expression : function_class SEMI\n    \n    expression : inside SEMI\n    \n    expression : empty\n    \n    error_handling : try catch\n    \n    try : TRY LMB expression RMB\n    \n    catch : CATCH LSB IDENTIFIER RSB LMB expression RMB\n    \n    for : for_head for_body\n    \n    for_head : FOR LSB IDENTIFIER IN IDENTIFIER RSB\n    \n    for_body : LMB expression RMB\n    \n    while : while_head while_body\n    \n    while_head : WHILE LSB condition RSB\n    \n    while_body : LMB expression RMB\n    \n    repeat : repeat_head repeat_body\n    \n    repeat_head : REPEAT LSB calculate RSB\n    \n    repeat_body : LMB expression RMB\n    \n    inside : inside DOT IDENTIFIER LSB parameter RSB\n    \n    inside : inside DOT IDENTIFIER\n    \n    inside : IDENTIFIER LSB parameter RSB\n    \n    inside : IDENTIFIER\n    \n    function_class : VAR IDENTIFIER EQUAL IDENTIFIER LSB parameter RSB\n        | VAR IDENTIFIER EQUAL IDENTIFIER LSB empty RSB\n    \n    function_class : IDENTIFIER EQUAL IDENTIFIER LSB parameter RSB\n        | IDENTIFIER EQUAL IDENTIFIER LSB empty RSB\n    \n    class_def : CLASS IDENTIFIER LMB expression RMB\n    \n    function : function_head function_body\n    \n    function_head : FUNCTION IDENTIFIER LSB parameter RSB\n        | FUNCTION IDENTIFIER LSB empty RSB\n    \n    function_body : LMB expression RMB\n    \n    parameter : parameter COMMA calculate\n    \n    parameter : calculate\n    \n    debug : USE DEBUG\n    \n    if_statement : if_statement_1 if_statement_2 if_statement_3\n        | if_statement_1 if_statement_2\n        | if_statement_1 if_statement_3\n        | if_statement_1\n    \n    if_statement_1 : IF LSB condition RSB LMB expression RMB\n    \n    if_statement_2 : ELSE IF LSB condition RSB LMB expression RMB\n    \n    if_statement_2 : if_statement_2 ELSE IF LSB condition RSB LMB expression RMB\n    \n    if_statement_3 : ELSE LMB expression RMB\n    \n    condition : condition LB calculate\n        | condition RB calculate\n    \n    condition : condition LB EQUAL calculate\n        | condition RB EQUAL calculate\n    \n    condition : condition EQUAL calculate\n    \n    condition : calculate\n    \n    use : USE use_params\n    \n    use_params : IDENTIFIER\n    \n    global_variable : GLOBAL IDENTIFIER\n    \n    variable_alone : IDENTIFIER\n    \n    variable_value_change : IDENTIFIER EQUAL LIST\n    \n    variable_value_change : IDENTIFIER EQUAL calculate\n    \n    variable_declaration : VAR IDENTIFIER LIST EQUAL calculate\n    \n    variable_declaration : VAR IDENTIFIER EQUAL calculate\n    \n    variable_declaration : VAR IDENTIFIER\n    calculate : calculate PLUS calculatecalculate : calculate MINUS calculatecalculate : MINUS calculate %prec UMINUS\n    calculate : calculate MUL calculate\n        | calculate DIV calculate\n    \n    calculate : INT\n        | FLOAT\n        | STRING\n    \n    calculate : IDENTIFIER\n    \n    calculate : IDENTIFIER LIST\n    \n    calculate : LIST\n    calculate : LSB calculate RSBempty : '
    
_lr_action_items = {'VAR':([0,2,5,6,7,8,9,11,14,18,21,38,39,40,41,42,44,47,51,52,53,54,55,56,57,58,63,64,66,67,68,69,70,71,72,73,77,86,87,88,89,90,91,92,93,94,110,113,114,115,116,117,119,126,143,144,145,146,147,149,173,175,176,192,193,200,201,202,203,204,205,206,207,208,],[19,19,-19,-20,-21,-22,-23,-25,-28,-32,-64,-4,-5,-6,-7,-8,-10,-13,-17,-18,-24,-26,-27,-29,-30,-31,-62,-63,-54,19,-42,19,-36,19,-39,19,-33,19,-2,-3,-9,-11,-12,-14,-15,-16,-61,19,19,19,19,19,19,19,19,-57,-44,-38,-41,19,-68,-53,19,19,19,19,19,-65,19,19,-35,19,-66,-67,]),'IDENTIFIER':([0,2,5,6,7,8,9,11,14,18,19,21,26,28,29,31,38,39,40,41,42,44,47,51,52,53,54,55,56,57,58,59,61,62,63,64,66,67,68,69,70,71,72,73,77,81,83,84,85,86,87,88,89,90,91,92,93,94,97,101,102,110,113,114,115,116,117,118,119,122,126,127,128,131,133,134,135,136,140,142,143,144,145,146,147,149,151,152,153,157,162,171,173,175,176,178,180,192,193,200,201,202,203,204,205,206,207,208,],[20,20,-19,-20,-21,-22,-23,-25,-28,-32,60,-64,76,79,80,82,-4,-5,-6,-7,-8,-10,-13,-17,-18,-24,-26,-27,-29,-30,-31,95,98,106,-62,-63,-54,20,-42,20,-36,20,-39,20,-33,106,106,124,106,20,-2,-3,-9,-11,-12,-14,-15,-16,129,106,106,-61,20,20,20,20,20,148,20,106,20,106,106,106,106,106,106,106,106,106,20,-57,-44,-38,-41,20,106,106,106,184,106,106,-68,-53,20,106,106,20,20,20,20,-65,20,20,-35,20,-66,-67,]),'USE':([0,2,5,6,7,8,9,11,14,18,21,38,39,40,41,42,44,47,51,52,53,54,55,56,57,58,63,64,66,67,68,69,70,71,72,73,77,86,87,88,89,90,91,92,93,94,110,113,114,115,116,117,119,126,143,144,145,146,147,149,173,175,176,192,193,200,201,202,203,204,205,206,207,208,],[26,26,-19,-20,-21,-22,-23,-25,-28,-32,-64,-4,-5,-6,-7,-8,-10,-13,-17,-18,-24,-26,-27,-29,-30,-31,-62,-63,-54,26,-42,26,-36,26,-39,26,-33,26,-2,-3,-9,-11,-12,-14,-15,-16,-61,26,26,26,26,26,26,26,26,-57,-44,-38,-41,26,-68,-53,26,26,26,26,26,-65,26,26,-35,26,-66,-67,]),'GLOBAL':([0,2,5,6,7,8,9,11,14,18,21,38,39,40,41,42,44,47,51,52,53,54,55,56,57,58,63,64,66,67,68,69,70,71,72,73,77,86,87,88,89,90,91,92,93,94,110,113,114,115,116,117,119,126,143,144,145,146,147,149,173,175,176,192,193,200,201,202,203,204,205,206,207,208,],[28,28,-19,-20,-21,-22,-23,-25,-28,-32,-64,-4,-5,-6,-7,-8,-10,-13,-17,-18,-24,-26,-27,-29,-30,-31,-62,-63,-54,28,-42,28,-36,28,-39,28,-33,28,-2,-3,-9,-11,-12,-14,-15,-16,-61,28,28,28,28,28,28,28,28,-57,-44,-38,-41,28,-68,-53,28,28,28,28,28,-65,28,28,-35,28,-66,-67,]),'CLASS':([0,2,5,6,7,8,9,11,14,18,21,38,39,40,41,42,44,47,51,52,53,54,55,56,57,58,63,64,66,67,68,69,70,71,72,73,77,86,87,88,89,90,91,92,93,94,110,113,114,115,116,117,119,126,143,144,145,146,147,149,173,175,176,192,193,200,201,202,203,204,205,206,207,208,],[29,29,-19,-20,-21,-22,-23,-25,-28,-32,-64,-4,-5,-6,-7,-8,-10,-13,-17,-18,-24,-26,-27,-29,-30,-31,-62,-63,-54,29,-42,29,-36,29,-39,29,-33,29,-2,-3,-9,-11,-12,-14,-15,-16,-61,29,29,29,29,29,29,29,29,-57,-44,-38,-41,29,-68,-53,29,29,29,29,29,-65,29,29,-35,29,-66,-67,]),'IF':([0,2,5,6,7,8,9,11,14,18,21,38,39,40,41,42,44,47,51,52,53,54,55,56,57,58,63,64,65,66,67,68,69,70,71,72,73,77,86,87,88,89,90,91,92,93,94,110,111,113,114,115,116,117,119,126,143,144,145,146,147,149,173,175,176,192,193,200,201,202,203,204,205,206,207,208,],[30,30,-19,-20,-21,-22,-23,-25,-28,-32,-64,-4,-5,-6,-7,-8,-10,-13,-17,-18,-24,-26,-27,-29,-30,-31,-62,-63,112,-54,30,-42,30,-36,30,-39,30,-33,30,-2,-3,-9,-11,-12,-14,-15,-16,-61,141,30,30,30,30,30,30,30,30,-57,-44,-38,-41,30,-68,-53,30,30,30,30,30,-65,30,30,-35,30,-66,-67,]),'FUNCTION':([0,2,5,6,7,8,9,11,14,18,21,38,39,40,41,42,44,47,51,52,53,54,55,56,57,58,63,64,66,67,68,69,70,71,72,73,77,86,87,88,89,90,91,92,93,94,110,113,114,115,116,117,119,126,143,144,145,146,147,149,173,175,176,192,193,200,201,202,203,204,205,206,207,208,],[31,31,-19,-20,-21,-22,-23,-25,-28,-32,-64,-4,-5,-6,-7,-8,-10,-13,-17,-18,-24,-26,-27,-29,-30,-31,-62,-63,-54,31,-42,31,-36,31,-39,31,-33,31,-2,-3,-9,-11,-12,-14,-15,-16,-61,31,31,31,31,31,31,31,31,-57,-44,-38,-41,31,-68,-53,31,31,31,31,31,-65,31,31,-35,31,-66,-67,]),'REPEAT':([0,2,5,6,7,8,9,11,14,18,21,38,39,40,41,42,44,47,51,52,53,54,55,56,57,58,63,64,66,67,68,69,70,71,72,73,77,86,87,88,89,90,91,92,93,94,110,113,114,115,116,117,119,126,143,144,145,146,147,149,173,175,176,192,193,200,201,202,203,204,205,206,207,208,],[32,32,-19,-20,-21,-22,-23,-25,-28,-32,-64,-4,-5,-6,-7,-8,-10,-13,-17,-18,-24,-26,-27,-29,-30,-31,-62,-63,-54,32,-42,32,-36,32,-39,32,-33,32,-2,-3,-9,-11,-12,-14,-15,-16,-61,32,32,32,32,32,32,32,32,-57,-44,-38,-41,32,-68,-53,32,32,32,32,32,-65,32,32,-35,32,-66,-67,]),'FOR':([0,2,5,6,7,8,9,11,14,18,21,38,39,40,41,42,44,47,51,52,53,54,55,56,57,58,63,64,66,67,68,69,70,71,72,73,77,86,87,88,89,90,91,92,93,94,110,113,114,115,116,117,119,126,143,144,145,146,147,149,173,175,176,192,193,200,201,202,203,204,205,206,207,208,],[33,33,-19,-20,-21,-22,-23,-25,-28,-32,-64,-4,-5,-6,-7,-8,-10,-13,-17,-18,-24,-26,-27,-29,-30,-31,-62,-63,-54,33,-42,33,-36,33,-39,33,-33,33,-2,-3,-9,-11,-12,-14,-15,-16,-61,33,33,33,33,33,33,33,33,-57,-44,-38,-41,33,-68,-53,33,33,33,33,33,-65,33,33,-35,33,-66,-67,]),'WHILE':([0,2,5,6,7,8,9,11,14,18,21,38,39,40,41,42,44,47,51,52,53,54,55,56,57,58,63,64,66,67,68,69,70,71,72,73,77,86,87,88,89,90,91,92,93,94,110,113,114,115,116,117,119,126,143,144,145,146,147,149,173,175,176,192,193,200,201,202,203,204,205,206,207,208,],[34,34,-19,-20,-21,-22,-23,-25,-28,-32,-64,-4,-5,-6,-7,-8,-10,-13,-17,-18,-24,-26,-27,-29,-30,-31,-62,-63,-54,34,-42,34,-36,34,-39,34,-33,34,-2,-3,-9,-11,-12,-14,-15,-16,-61,34,34,34,34,34,34,34,34,-57,-44,-38,-41,34,-68,-53,34,34,34,34,34,-65,34,34,-35,34,-66,-67,]),'TRY':([0,2,5,6,7,8,9,11,14,18,21,38,39,40,41,42,44,47,51,52,53,54,55,56,57,58,63,64,66,67,68,69,70,71,72,73,77,86,87,88,89,90,91,92,93,94,110,113,114,115,116,117,119,126,143,144,145,146,147,149,173,175,176,192,193,200,201,202,203,204,205,206,207,208,],[35,35,-19,-20,-21,-22,-23,-25,-28,-32,-64,-4,-5,-6,-7,-8,-10,-13,-17,-18,-24,-26,-27,-29,-30,-31,-62,-63,-54,35,-42,35,-36,35,-39,35,-33,35,-2,-3,-9,-11,-12,-14,-15,-16,-61,35,35,35,35,35,35,35,35,-57,-44,-38,-41,35,-68,-53,35,35,35,35,35,-65,35,35,-35,35,-66,-67,]),'$end':([0,1,2,5,6,7,8,9,11,14,18,21,38,39,40,41,42,44,47,51,52,53,54,55,56,57,58,63,64,66,68,70,72,77,87,88,89,90,91,92,93,94,110,144,145,146,147,173,175,202,205,207,208,],[-96,0,-1,-19,-20,-21,-22,-23,-25,-28,-32,-64,-4,-5,-6,-7,-8,-10,-13,-17,-18,-24,-26,-27,-29,-30,-31,-62,-63,-54,-42,-36,-39,-33,-2,-3,-9,-11,-12,-14,-15,-16,-61,-57,-44,-38,-41,-68,-53,-65,-35,-66,-67,]),'SEMI':([3,4,10,12,13,15,16,17,20,36,37,43,45,46,48,49,50,60,74,75,76,79,95,98,99,100,103,104,105,106,109,129,130,132,138,139,161,165,166,167,168,169,185,188,189,197,198,],[51,52,53,54,55,56,57,58,-48,87,88,89,90,91,92,93,94,-83,-75,-60,-76,-77,-46,-92,-79,-80,-89,-90,-91,-92,-94,-92,-82,-93,-86,-47,-81,-84,-85,-87,-88,-95,-45,-51,-52,-49,-50,]),'RMB':([5,6,7,8,9,11,14,18,21,38,39,40,41,42,44,47,51,52,53,54,55,56,57,58,63,64,66,67,68,69,70,71,72,73,77,86,87,88,89,90,91,92,93,94,110,113,114,115,116,117,119,126,143,144,145,146,147,149,173,175,176,192,193,200,201,202,203,204,205,206,207,208,],[-19,-20,-21,-22,-23,-25,-28,-32,-64,-4,-5,-6,-7,-8,-10,-13,-17,-18,-24,-26,-27,-29,-30,-31,-62,-63,-54,-96,-42,-96,-36,-96,-39,-96,-33,-96,-2,-3,-9,-11,-12,-14,-15,-16,-61,-96,144,145,146,147,-96,159,173,-57,-44,-38,-41,175,-68,-53,-96,-96,202,-96,205,-65,-96,207,-35,208,-66,-67,]),'DOT':([17,20,50,95,139,185,],[59,-48,59,-46,-47,-45,]),'EQUAL':([20,60,96,103,104,105,106,109,120,121,125,132,138,151,152,165,166,167,168,169,172,177,179,181,190,194,195,],[61,97,128,-89,-90,-91,-92,-94,153,-74,153,-93,-86,178,180,-84,-85,-87,-88,-95,153,-69,-70,-73,153,-71,-72,]),'LSB':([20,30,32,33,34,61,62,78,81,82,83,85,95,97,98,101,102,112,122,127,128,129,131,133,134,135,136,140,141,142,151,152,153,162,171,178,180,],[62,81,83,84,85,101,101,118,101,122,101,101,127,101,131,101,101,142,101,101,101,162,101,101,101,101,101,101,171,101,101,101,101,101,101,101,101,]),'ELSE':([21,63,202,207,208,],[65,111,-65,-66,-67,]),'LMB':([22,23,24,25,35,65,80,111,150,156,158,174,182,183,191,196,199,],[67,69,71,73,86,113,119,113,176,-43,-40,192,-55,-56,200,-37,203,]),'DEBUG':([26,],[75,]),'CATCH':([27,159,],[78,-34,]),'LIST':([60,61,62,81,83,85,97,98,101,102,106,122,127,128,129,131,133,134,135,136,140,142,151,152,153,162,171,178,180,],[96,99,109,109,109,109,109,132,109,109,132,109,109,109,132,109,109,109,109,109,109,109,109,109,109,109,109,109,109,]),'MINUS':([61,62,81,83,85,97,98,99,100,101,102,103,104,105,106,108,109,121,122,123,127,128,129,130,131,132,133,134,135,136,137,138,140,142,151,152,153,161,162,165,166,167,168,169,170,171,177,178,179,180,181,194,195,],[102,102,102,102,102,102,-92,-94,134,102,102,-89,-90,-91,-92,134,-94,134,102,134,102,102,-92,134,102,-93,102,102,102,102,134,-86,102,102,102,102,102,134,102,-84,-85,-87,-88,-95,134,102,134,102,134,102,134,134,134,]),'INT':([61,62,81,83,85,97,101,102,122,127,128,131,133,134,135,136,140,142,151,152,153,162,171,178,180,],[103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,]),'FLOAT':([61,62,81,83,85,97,101,102,122,127,128,131,133,134,135,136,140,142,151,152,153,162,171,178,180,],[104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,]),'STRING':([61,62,81,83,85,97,101,102,122,127,128,131,133,134,135,136,140,142,151,152,153,162,171,178,180,],[105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,]),'PLUS':([98,99,100,103,104,105,106,108,109,121,123,129,130,132,137,138,161,165,166,167,168,169,170,177,179,181,194,195,],[-92,-94,133,-89,-90,-91,-92,133,-94,133,133,-92,133,-93,133,-86,133,-84,-85,-87,-88,-95,133,133,133,133,133,133,]),'MUL':([98,99,100,103,104,105,106,108,109,121,123,129,130,132,137,138,161,165,166,167,168,169,170,177,179,181,194,195,],[-92,-94,135,-89,-90,-91,-92,135,-94,135,135,-92,135,-93,135,-86,135,135,135,-87,-88,-95,135,135,135,135,135,135,]),'DIV':([98,99,100,103,104,105,106,108,109,121,123,129,130,132,137,138,161,165,166,167,168,169,170,177,179,181,194,195,],[-92,-94,136,-89,-90,-91,-92,136,-94,136,136,-92,136,-93,136,-86,136,136,136,-87,-88,-95,136,136,136,136,136,136,]),'RSB':([103,104,105,106,107,108,109,120,121,122,123,125,131,132,137,138,148,154,155,160,162,163,164,165,166,167,168,169,170,172,177,179,181,184,186,187,190,194,195,],[-89,-90,-91,-92,139,-59,-94,150,-74,-96,156,158,-96,-93,169,-86,174,182,183,185,-96,188,189,-84,-85,-87,-88,-95,-58,191,-69,-70,-73,196,197,198,199,-71,-72,]),'COMMA':([103,104,105,106,107,108,109,132,138,154,160,163,165,166,167,168,169,170,186,],[-89,-90,-91,-92,140,-59,-94,-93,-86,140,140,140,-84,-85,-87,-88,-95,-58,140,]),'LB':([103,104,105,106,109,120,121,125,132,138,165,166,167,168,169,172,177,179,181,190,194,195,],[-89,-90,-91,-92,-94,151,-74,151,-93,-86,-84,-85,-87,-88,-95,151,-69,-70,-73,151,-71,-72,]),'RB':([103,104,105,106,109,120,121,125,132,138,165,166,167,168,169,172,177,179,181,190,194,195,],[-89,-90,-91,-92,-94,152,-74,152,-93,-86,-84,-85,-87,-88,-95,152,-69,-70,-73,152,-71,-72,]),'IN':([124,],[157,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'root':([0,],[1,]),'expression':([0,67,69,71,73,86,113,119,176,192,200,203,],[2,114,115,116,117,126,143,149,193,201,204,206,]),'variable_declaration':([0,2,67,69,71,73,86,113,114,115,116,117,119,126,143,149,176,192,193,200,201,203,204,206,],[3,36,3,3,3,3,3,3,36,36,36,36,3,36,36,36,3,3,36,3,36,3,36,36,]),'variable_value_change':([0,2,67,69,71,73,86,113,114,115,116,117,119,126,143,149,176,192,193,200,201,203,204,206,],[4,37,4,4,4,4,4,4,37,37,37,37,4,37,37,37,4,4,37,4,37,4,37,37,]),'if_statement':([0,2,67,69,71,73,86,113,114,115,116,117,119,126,143,149,176,192,193,200,201,203,204,206,],[5,38,5,5,5,5,5,5,38,38,38,38,5,38,38,38,5,5,38,5,38,5,38,38,]),'function':([0,2,67,69,71,73,86,113,114,115,116,117,119,126,143,149,176,192,193,200,201,203,204,206,],[6,39,6,6,6,6,6,6,39,39,39,39,6,39,39,39,6,6,39,6,39,6,39,39,]),'repeat':([0,2,67,69,71,73,86,113,114,115,116,117,119,126,143,149,176,192,193,200,201,203,204,206,],[7,40,7,7,7,7,7,7,40,40,40,40,7,40,40,40,7,7,40,7,40,7,40,40,]),'for':([0,2,67,69,71,73,86,113,114,115,116,117,119,126,143,149,176,192,193,200,201,203,204,206,],[8,41,8,8,8,8,8,8,41,41,41,41,8,41,41,41,8,8,41,8,41,8,41,41,]),'while':([0,2,67,69,71,73,86,113,114,115,116,117,119,126,143,149,176,192,193,200,201,203,204,206,],[9,42,9,9,9,9,9,9,42,42,42,42,9,42,42,42,9,9,42,9,42,9,42,42,]),'use':([0,2,67,69,71,73,86,113,114,115,116,117,119,126,143,149,176,192,193,200,201,203,204,206,],[10,43,10,10,10,10,10,10,43,43,43,43,10,43,43,43,10,10,43,10,43,10,43,43,]),'error_handling':([0,2,67,69,71,73,86,113,114,115,116,117,119,126,143,149,176,192,193,200,201,203,204,206,],[11,44,11,11,11,11,11,11,44,44,44,44,11,44,44,44,11,11,44,11,44,11,44,44,]),'variable_alone':([0,2,67,69,71,73,86,113,114,115,116,117,119,126,143,149,176,192,193,200,201,203,204,206,],[12,45,12,12,12,12,12,12,45,45,45,45,12,45,45,45,12,12,45,12,45,12,45,45,]),'global_variable':([0,2,67,69,71,73,86,113,114,115,116,117,119,126,143,149,176,192,193,200,201,203,204,206,],[13,46,13,13,13,13,13,13,46,46,46,46,13,46,46,46,13,13,46,13,46,13,46,46,]),'class_def':([0,2,67,69,71,73,86,113,114,115,116,117,119,126,143,149,176,192,193,200,201,203,204,206,],[14,47,14,14,14,14,14,14,47,47,47,47,14,47,47,47,14,14,47,14,47,14,47,47,]),'debug':([0,2,67,69,71,73,86,113,114,115,116,117,119,126,143,149,176,192,193,200,201,203,204,206,],[15,48,15,15,15,15,15,15,48,48,48,48,15,48,48,48,15,15,48,15,48,15,48,48,]),'function_class':([0,2,67,69,71,73,86,113,114,115,116,117,119,126,143,149,176,192,193,200,201,203,204,206,],[16,49,16,16,16,16,16,16,49,49,49,49,16,49,49,49,16,16,49,16,49,16,49,49,]),'inside':([0,2,67,69,71,73,86,113,114,115,116,117,119,126,143,149,176,192,193,200,201,203,204,206,],[17,50,17,17,17,17,17,17,50,50,50,50,17,50,50,50,17,17,50,17,50,17,50,50,]),'empty':([0,67,69,71,73,86,113,119,122,131,162,176,192,200,203,],[18,18,18,18,18,18,18,18,155,164,187,18,18,18,18,]),'if_statement_1':([0,2,67,69,71,73,86,113,114,115,116,117,119,126,143,149,176,192,193,200,201,203,204,206,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'function_head':([0,2,67,69,71,73,86,113,114,115,116,117,119,126,143,149,176,192,193,200,201,203,204,206,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'repeat_head':([0,2,67,69,71,73,86,113,114,115,116,117,119,126,143,149,176,192,193,200,201,203,204,206,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'for_head':([0,2,67,69,71,73,86,113,114,115,116,117,119,126,143,149,176,192,193,200,201,203,204,206,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'while_head':([0,2,67,69,71,73,86,113,114,115,116,117,119,126,143,149,176,192,193,200,201,203,204,206,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'try':([0,2,67,69,71,73,86,113,114,115,116,117,119,126,143,149,176,192,193,200,201,203,204,206,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'if_statement_2':([21,],[63,]),'if_statement_3':([21,63,],[64,110,]),'function_body':([22,],[66,]),'repeat_body':([23,],[68,]),'for_body':([24,],[70,]),'while_body':([25,],[72,]),'use_params':([26,],[74,]),'catch':([27,],[77,]),'calculate':([61,62,81,83,85,97,101,102,122,127,128,131,133,134,135,136,140,142,151,152,153,162,171,178,180,],[100,108,121,123,121,130,137,138,108,108,161,108,165,166,167,168,170,121,177,179,181,108,121,194,195,]),'parameter':([62,122,127,131,162,],[107,154,160,163,186,]),'condition':([81,85,142,171,],[120,125,172,190,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> root","S'",1,None,None,None),
  ('root -> expression','root',1,'p_root','main.py',157),
  ('expression -> expression variable_declaration SEMI','expression',3,'p_expression_variable','main.py',171),
  ('expression -> expression variable_value_change SEMI','expression',3,'p_expression_variable','main.py',172),
  ('expression -> expression if_statement','expression',2,'p_expression_if_statement','main.py',189),
  ('expression -> expression function','expression',2,'p_expression_function','main.py',200),
  ('expression -> expression repeat','expression',2,'p_expression_repeat','main.py',206),
  ('expression -> expression for','expression',2,'p_expression_for','main.py',212),
  ('expression -> expression while','expression',2,'p_expression_while','main.py',218),
  ('expression -> expression use SEMI','expression',3,'p_expression_use','main.py',224),
  ('expression -> expression error_handling','expression',2,'p_expression_error_handling','main.py',230),
  ('expression -> expression variable_alone SEMI','expression',3,'p_expression_variable_alone','main.py',236),
  ('expression -> expression global_variable SEMI','expression',3,'p_expression_global_variable','main.py',242),
  ('expression -> expression class_def','expression',2,'p_expression_class_def','main.py',248),
  ('expression -> expression debug SEMI','expression',3,'p_expression_debug','main.py',254),
  ('expression -> expression function_class SEMI','expression',3,'p_expression_function_class','main.py',260),
  ('expression -> expression inside SEMI','expression',3,'p_expression_inside','main.py',266),
  ('expression -> variable_declaration SEMI','expression',2,'p_expression_variable_2','main.py',274),
  ('expression -> variable_value_change SEMI','expression',2,'p_expression_variable_2','main.py',275),
  ('expression -> if_statement','expression',1,'p_expression_if_statement_2','main.py',286),
  ('expression -> function','expression',1,'p_expression_function_2','main.py',294),
  ('expression -> repeat','expression',1,'p_expression_repeat_2','main.py',300),
  ('expression -> for','expression',1,'p_expression_for_2','main.py',306),
  ('expression -> while','expression',1,'p_expression_while_2','main.py',312),
  ('expression -> use SEMI','expression',2,'p_expression_use_2','main.py',318),
  ('expression -> error_handling','expression',1,'p_expression_error_handling_2','main.py',324),
  ('expression -> variable_alone SEMI','expression',2,'p_expression_variable_alone_2','main.py',330),
  ('expression -> global_variable SEMI','expression',2,'p_expression_global_variable_2','main.py',336),
  ('expression -> class_def','expression',1,'p_expression_class_def_2','main.py',342),
  ('expression -> debug SEMI','expression',2,'p_expression_debug_2','main.py',348),
  ('expression -> function_class SEMI','expression',2,'p_expression_function_class_2','main.py',354),
  ('expression -> inside SEMI','expression',2,'p_expression_inside_2','main.py',360),
  ('expression -> empty','expression',1,'p_expression_empty','main.py',368),
  ('error_handling -> try catch','error_handling',2,'p_error_handling','main.py',377),
  ('try -> TRY LMB expression RMB','try',4,'p_try','main.py',383),
  ('catch -> CATCH LSB IDENTIFIER RSB LMB expression RMB','catch',7,'p_catch','main.py',394),
  ('for -> for_head for_body','for',2,'p_for','main.py',407),
  ('for_head -> FOR LSB IDENTIFIER IN IDENTIFIER RSB','for_head',6,'p_for_head','main.py',415),
  ('for_body -> LMB expression RMB','for_body',3,'p_for_body','main.py',421),
  ('while -> while_head while_body','while',2,'p_while','main.py',432),
  ('while_head -> WHILE LSB condition RSB','while_head',4,'p_while_head','main.py',440),
  ('while_body -> LMB expression RMB','while_body',3,'p_while_body','main.py',446),
  ('repeat -> repeat_head repeat_body','repeat',2,'p_repeat','main.py',458),
  ('repeat_head -> REPEAT LSB calculate RSB','repeat_head',4,'p_repeat_head','main.py',466),
  ('repeat_body -> LMB expression RMB','repeat_body',3,'p_repeat_body','main.py',472),
  ('inside -> inside DOT IDENTIFIER LSB parameter RSB','inside',6,'p_inside','main.py',483),
  ('inside -> inside DOT IDENTIFIER','inside',3,'p_inside_2','main.py',489),
  ('inside -> IDENTIFIER LSB parameter RSB','inside',4,'p_inside_3','main.py',495),
  ('inside -> IDENTIFIER','inside',1,'p_inside_4','main.py',501),
  ('function_class -> VAR IDENTIFIER EQUAL IDENTIFIER LSB parameter RSB','function_class',7,'p_function_class_declaration','main.py',509),
  ('function_class -> VAR IDENTIFIER EQUAL IDENTIFIER LSB empty RSB','function_class',7,'p_function_class_declaration','main.py',510),
  ('function_class -> IDENTIFIER EQUAL IDENTIFIER LSB parameter RSB','function_class',6,'p_function_class_call','main.py',519),
  ('function_class -> IDENTIFIER EQUAL IDENTIFIER LSB empty RSB','function_class',6,'p_function_class_call','main.py',520),
  ('class_def -> CLASS IDENTIFIER LMB expression RMB','class_def',5,'p_class_def','main.py',531),
  ('function -> function_head function_body','function',2,'p_function','main.py',546),
  ('function_head -> FUNCTION IDENTIFIER LSB parameter RSB','function_head',5,'p_function_head','main.py',554),
  ('function_head -> FUNCTION IDENTIFIER LSB empty RSB','function_head',5,'p_function_head','main.py',555),
  ('function_body -> LMB expression RMB','function_body',3,'p_function_body','main.py',564),
  ('parameter -> parameter COMMA calculate','parameter',3,'p_parameter','main.py',587),
  ('parameter -> calculate','parameter',1,'p_parameter_2','main.py',593),
  ('debug -> USE DEBUG','debug',2,'p_debug','main.py',605),
  ('if_statement -> if_statement_1 if_statement_2 if_statement_3','if_statement',3,'p_if_statement','main.py',615),
  ('if_statement -> if_statement_1 if_statement_2','if_statement',2,'p_if_statement','main.py',616),
  ('if_statement -> if_statement_1 if_statement_3','if_statement',2,'p_if_statement','main.py',617),
  ('if_statement -> if_statement_1','if_statement',1,'p_if_statement','main.py',618),
  ('if_statement_1 -> IF LSB condition RSB LMB expression RMB','if_statement_1',7,'p_if_statement_1','main.py',630),
  ('if_statement_2 -> ELSE IF LSB condition RSB LMB expression RMB','if_statement_2',8,'p_if_statement_2','main.py',639),
  ('if_statement_2 -> if_statement_2 ELSE IF LSB condition RSB LMB expression RMB','if_statement_2',9,'p_if_statement_2_2','main.py',650),
  ('if_statement_3 -> ELSE LMB expression RMB','if_statement_3',4,'p_if_statement_3','main.py',661),
  ('condition -> condition LB calculate','condition',3,'p_condition','main.py',674),
  ('condition -> condition RB calculate','condition',3,'p_condition','main.py',675),
  ('condition -> condition LB EQUAL calculate','condition',4,'p_condition_2','main.py',681),
  ('condition -> condition RB EQUAL calculate','condition',4,'p_condition_2','main.py',682),
  ('condition -> condition EQUAL calculate','condition',3,'p_condition_3','main.py',688),
  ('condition -> calculate','condition',1,'p_condition_4','main.py',694),
  ('use -> USE use_params','use',2,'p_use','main.py',704),
  ('use_params -> IDENTIFIER','use_params',1,'p_use_params','main.py',727),
  ('global_variable -> GLOBAL IDENTIFIER','global_variable',2,'p_global_variable','main.py',734),
  ('variable_alone -> IDENTIFIER','variable_alone',1,'p_variable_alone','main.py',742),
  ('variable_value_change -> IDENTIFIER EQUAL LIST','variable_value_change',3,'p_variable_value_change_list','main.py',750),
  ('variable_value_change -> IDENTIFIER EQUAL calculate','variable_value_change',3,'p_variable_value_change','main.py',756),
  ('variable_declaration -> VAR IDENTIFIER LIST EQUAL calculate','variable_declaration',5,'p_variable_declaration_list','main.py',784),
  ('variable_declaration -> VAR IDENTIFIER EQUAL calculate','variable_declaration',4,'p_variable_declaration_2','main.py',790),
  ('variable_declaration -> VAR IDENTIFIER','variable_declaration',2,'p_variable_declaration_1','main.py',806),
  ('calculate -> calculate PLUS calculate','calculate',3,'p_add','main.py',835),
  ('calculate -> calculate MINUS calculate','calculate',3,'p_sub','main.py',871),
  ('calculate -> MINUS calculate','calculate',2,'p_calculate2uminus','main.py',875),
  ('calculate -> calculate MUL calculate','calculate',3,'p_mul_div','main.py',880),
  ('calculate -> calculate DIV calculate','calculate',3,'p_mul_div','main.py',881),
  ('calculate -> INT','calculate',1,'p_calculate2num','main.py',892),
  ('calculate -> FLOAT','calculate',1,'p_calculate2num','main.py',893),
  ('calculate -> STRING','calculate',1,'p_calculate2num','main.py',894),
  ('calculate -> IDENTIFIER','calculate',1,'p_calculate2str','main.py',900),
  ('calculate -> IDENTIFIER LIST','calculate',2,'p_calculate2list','main.py',909),
  ('calculate -> LIST','calculate',1,'p_calculate2list_2','main.py',915),
  ('calculate -> LSB calculate RSB','calculate',3,'p_parens','main.py',920),
  ('empty -> <empty>','empty',0,'p_empty','main.py',926),
]
