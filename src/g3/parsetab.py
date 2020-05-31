
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftMULDIVrightUMINUSCATCH CLASS COLON COMMA DEBUG DIV DOT ELSE EQUAL FLOAT FOR FUNCTION GLOBAL IDENTIFIER IF IN INPUT INT LB LIST LMB LSB MINUS MUL PLUS PRINT PYTHON RB REPEAT RMB RSB SEMI STRING TRY USE VAR WHILE\n    root : expression\n    \n    expression : expression variable_declaration SEMI\n        | expression variable_value_change SEMI\n    \n    expression : expression if_statement\n    \n    expression : expression function\n    \n    expression : expression function_call SEMI\n    \n    expression : expression repeat\n    \n    expression : expression for\n    \n    expression : expression while\n    \n    expression : expression use SEMI\n    \n    expression : expression error_handling\n    \n    expression : expression variable_alone SEMI\n    \n    expression : expression global_variable SEMI\n    \n    expression : expression class_def\n    \n    expression : expression debug SEMI\n    \n    expression : expression function_class SEMI\n    \n    expression : expression inside_root SEMI\n    \n    expression : variable_declaration SEMI\n        | variable_value_change SEMI\n    \n    expression : if_statement\n    \n    expression : function\n    \n    expression : function_call SEMI\n    \n    expression : repeat\n    \n    expression : for\n    \n    expression : while\n    \n    expression : use SEMI\n    \n    expression : error_handling\n    \n    expression : variable_alone SEMI\n    \n    expression : global_variable SEMI\n    \n    expression : class_def\n    \n    expression : debug SEMI\n    \n    expression : function_class SEMI\n    \n    expression : inside_root SEMI\n    \n    expression : empty\n    \n    error_handling : try catch\n    \n    try : TRY LMB expression RMB\n    \n    catch : CATCH LSB IDENTIFIER RSB LMB expression RMB\n    \n    for : for_head for_body\n    \n    for_head : FOR LSB IDENTIFIER IN IDENTIFIER RSB\n    \n    for_body : LMB expression RMB\n    \n    while : while_head while_body\n    \n    while_head : WHILE LSB condition RSB\n    \n    while_body : LMB expression RMB\n    \n    repeat : repeat_head repeat_body\n    \n    repeat_head : REPEAT LSB calculate RSB\n    \n    repeat_body : LMB expression RMB\n    \n    inside_root : inside\n    \n    inside_root : inside DOT IDENTIFIER LSB parameter RSB\n    \n    inside : DOT IDENTIFIER LSB empty RSB\n    \n    inside : inside DOT IDENTIFIER\n    \n    inside : IDENTIFIER LSB parameter RSB DOT IDENTIFIER LSB parameter RSB\n    \n    inside : IDENTIFIER LSB empty RSB DOT IDENTIFIER LSB empty RSB\n    \n    inside : IDENTIFIER LSB parameter RSB DOT IDENTIFIER LSB empty RSB\n    \n    inside : IDENTIFIER LSB empty RSB DOT IDENTIFIER LSB parameter RSB\n    \n    inside : IDENTIFIER DOT IDENTIFIER LSB parameter RSB\n    \n    inside : IDENTIFIER DOT IDENTIFIER LSB empty RSB\n    \n    inside : IDENTIFIER LSB parameter DOT IDENTIFIER\n    \n    inside : IDENTIFIER DOT IDENTIFIER\n    \n    function_class : VAR IDENTIFIER EQUAL IDENTIFIER LSB parameter RSB\n        | VAR IDENTIFIER EQUAL IDENTIFIER LSB empty RSB\n    \n    function_class : IDENTIFIER EQUAL IDENTIFIER LSB parameter RSB\n        | IDENTIFIER EQUAL IDENTIFIER LSB empty RSB\n    \n    class_def : CLASS IDENTIFIER LMB expression RMB\n    \n    function : function_head function_body\n    \n    function_head : FUNCTION IDENTIFIER LSB parameter RSB\n        | FUNCTION IDENTIFIER LSB empty RSB\n    \n    function_body : LMB expression RMB\n    \n    function_call : IDENTIFIER LSB parameter RSB\n        | IDENTIFIER LSB empty RSB\n    \n    parameter : parameter COMMA calculate\n    \n    parameter : calculate\n    \n    debug : USE DEBUG\n    \n    if_statement : if_statement_1 if_statement_2 if_statement_3\n        | if_statement_1 if_statement_2\n        | if_statement_1 if_statement_3\n        | if_statement_1\n    \n    if_statement_1 : IF LSB condition RSB LMB expression RMB\n    \n    if_statement_2 : ELSE IF LSB condition RSB LMB expression RMB\n    \n    if_statement_2 : if_statement_2 ELSE IF LSB condition RSB LMB expression RMB\n    \n    if_statement_3 : ELSE LMB expression RMB\n    \n    condition : condition LB calculate\n        | condition RB calculate\n    \n    condition : condition LB EQUAL calculate\n        | condition RB EQUAL calculate\n    \n    condition : condition EQUAL calculate\n    \n    condition : calculate\n    \n    use : USE use_params\n    \n    use_params : IDENTIFIER\n    \n    global_variable : GLOBAL IDENTIFIER\n    \n    variable_alone : IDENTIFIER\n    \n    variable_value_change : IDENTIFIER EQUAL LIST\n    \n    variable_value_change : IDENTIFIER EQUAL calculate\n    \n    variable_declaration : VAR IDENTIFIER LIST EQUAL calculate\n    \n    variable_declaration : VAR IDENTIFIER EQUAL calculate\n    \n    variable_declaration : VAR IDENTIFIER\n    calculate : calculate PLUS calculatecalculate : calculate MINUS calculatecalculate : MINUS calculate %prec UMINUS\n    calculate : calculate MUL calculate\n        | calculate DIV calculate\n    \n    calculate : INT\n        | FLOAT\n        | STRING\n    \n    calculate : IDENTIFIER\n    \n    calculate : IDENTIFIER LIST\n    \n    calculate : LIST\n    calculate : LSB calculate RSBempty : '
    
_lr_action_items = {'VAR':([0,2,5,6,8,9,10,12,15,19,22,41,42,44,45,46,48,51,55,56,57,58,59,60,61,62,63,68,69,71,72,73,74,75,76,77,78,82,93,94,95,96,97,98,99,100,101,102,119,122,123,124,125,126,128,137,156,157,158,159,160,162,192,194,197,216,218,227,228,229,234,235,236,241,242,243,],[20,20,-20,-21,-23,-24,-25,-27,-30,-34,-76,-4,-5,-7,-8,-9,-11,-14,-18,-19,-22,-26,-28,-29,-31,-32,-33,-74,-75,-64,20,-44,20,-38,20,-41,20,-35,20,-2,-3,-6,-10,-12,-13,-15,-16,-17,-73,20,20,20,20,20,20,20,20,-67,-46,-40,-43,20,-80,-63,20,20,20,20,20,-77,20,20,-37,20,-78,-79,]),'IDENTIFIER':([0,2,5,6,8,9,10,12,15,19,20,22,27,29,30,32,34,41,42,44,45,46,48,51,55,56,57,58,59,60,61,62,63,65,66,67,68,69,71,72,73,74,75,76,77,78,82,86,88,90,91,92,93,94,95,96,97,98,99,100,101,102,104,108,109,119,122,123,124,125,126,127,128,133,137,138,141,143,144,145,146,150,151,153,155,156,157,158,159,160,162,163,166,167,168,172,176,184,187,190,192,194,197,199,201,216,218,224,225,227,228,229,234,235,236,241,242,243,],[21,21,-20,-21,-23,-24,-25,-27,-30,-34,64,-76,81,84,85,87,89,-4,-5,-7,-8,-9,-11,-14,-18,-19,-22,-26,-28,-29,-31,-32,-33,105,113,118,-74,-75,-64,21,-44,21,-38,21,-41,21,-35,129,113,113,135,113,21,-2,-3,-6,-10,-12,-13,-15,-16,-17,139,113,113,-73,21,21,21,21,21,161,21,113,21,113,113,113,113,113,113,185,113,113,113,21,-67,-46,-40,-43,21,113,113,113,113,205,113,210,211,113,-80,-63,21,113,113,21,21,113,113,21,21,-77,21,21,-37,21,-78,-79,]),'USE':([0,2,5,6,8,9,10,12,15,19,22,41,42,44,45,46,48,51,55,56,57,58,59,60,61,62,63,68,69,71,72,73,74,75,76,77,78,82,93,94,95,96,97,98,99,100,101,102,119,122,123,124,125,126,128,137,156,157,158,159,160,162,192,194,197,216,218,227,228,229,234,235,236,241,242,243,],[27,27,-20,-21,-23,-24,-25,-27,-30,-34,-76,-4,-5,-7,-8,-9,-11,-14,-18,-19,-22,-26,-28,-29,-31,-32,-33,-74,-75,-64,27,-44,27,-38,27,-41,27,-35,27,-2,-3,-6,-10,-12,-13,-15,-16,-17,-73,27,27,27,27,27,27,27,27,-67,-46,-40,-43,27,-80,-63,27,27,27,27,27,-77,27,27,-37,27,-78,-79,]),'GLOBAL':([0,2,5,6,8,9,10,12,15,19,22,41,42,44,45,46,48,51,55,56,57,58,59,60,61,62,63,68,69,71,72,73,74,75,76,77,78,82,93,94,95,96,97,98,99,100,101,102,119,122,123,124,125,126,128,137,156,157,158,159,160,162,192,194,197,216,218,227,228,229,234,235,236,241,242,243,],[29,29,-20,-21,-23,-24,-25,-27,-30,-34,-76,-4,-5,-7,-8,-9,-11,-14,-18,-19,-22,-26,-28,-29,-31,-32,-33,-74,-75,-64,29,-44,29,-38,29,-41,29,-35,29,-2,-3,-6,-10,-12,-13,-15,-16,-17,-73,29,29,29,29,29,29,29,29,-67,-46,-40,-43,29,-80,-63,29,29,29,29,29,-77,29,29,-37,29,-78,-79,]),'CLASS':([0,2,5,6,8,9,10,12,15,19,22,41,42,44,45,46,48,51,55,56,57,58,59,60,61,62,63,68,69,71,72,73,74,75,76,77,78,82,93,94,95,96,97,98,99,100,101,102,119,122,123,124,125,126,128,137,156,157,158,159,160,162,192,194,197,216,218,227,228,229,234,235,236,241,242,243,],[30,30,-20,-21,-23,-24,-25,-27,-30,-34,-76,-4,-5,-7,-8,-9,-11,-14,-18,-19,-22,-26,-28,-29,-31,-32,-33,-74,-75,-64,30,-44,30,-38,30,-41,30,-35,30,-2,-3,-6,-10,-12,-13,-15,-16,-17,-73,30,30,30,30,30,30,30,30,-67,-46,-40,-43,30,-80,-63,30,30,30,30,30,-77,30,30,-37,30,-78,-79,]),'IF':([0,2,5,6,8,9,10,12,15,19,22,41,42,44,45,46,48,51,55,56,57,58,59,60,61,62,63,68,69,70,71,72,73,74,75,76,77,78,82,93,94,95,96,97,98,99,100,101,102,119,120,122,123,124,125,126,128,137,156,157,158,159,160,162,192,194,197,216,218,227,228,229,234,235,236,241,242,243,],[33,33,-20,-21,-23,-24,-25,-27,-30,-34,-76,-4,-5,-7,-8,-9,-11,-14,-18,-19,-22,-26,-28,-29,-31,-32,-33,-74,-75,121,-64,33,-44,33,-38,33,-41,33,-35,33,-2,-3,-6,-10,-12,-13,-15,-16,-17,-73,154,33,33,33,33,33,33,33,33,-67,-46,-40,-43,33,-80,-63,33,33,33,33,33,-77,33,33,-37,33,-78,-79,]),'FUNCTION':([0,2,5,6,8,9,10,12,15,19,22,41,42,44,45,46,48,51,55,56,57,58,59,60,61,62,63,68,69,71,72,73,74,75,76,77,78,82,93,94,95,96,97,98,99,100,101,102,119,122,123,124,125,126,128,137,156,157,158,159,160,162,192,194,197,216,218,227,228,229,234,235,236,241,242,243,],[34,34,-20,-21,-23,-24,-25,-27,-30,-34,-76,-4,-5,-7,-8,-9,-11,-14,-18,-19,-22,-26,-28,-29,-31,-32,-33,-74,-75,-64,34,-44,34,-38,34,-41,34,-35,34,-2,-3,-6,-10,-12,-13,-15,-16,-17,-73,34,34,34,34,34,34,34,34,-67,-46,-40,-43,34,-80,-63,34,34,34,34,34,-77,34,34,-37,34,-78,-79,]),'REPEAT':([0,2,5,6,8,9,10,12,15,19,22,41,42,44,45,46,48,51,55,56,57,58,59,60,61,62,63,68,69,71,72,73,74,75,76,77,78,82,93,94,95,96,97,98,99,100,101,102,119,122,123,124,125,126,128,137,156,157,158,159,160,162,192,194,197,216,218,227,228,229,234,235,236,241,242,243,],[35,35,-20,-21,-23,-24,-25,-27,-30,-34,-76,-4,-5,-7,-8,-9,-11,-14,-18,-19,-22,-26,-28,-29,-31,-32,-33,-74,-75,-64,35,-44,35,-38,35,-41,35,-35,35,-2,-3,-6,-10,-12,-13,-15,-16,-17,-73,35,35,35,35,35,35,35,35,-67,-46,-40,-43,35,-80,-63,35,35,35,35,35,-77,35,35,-37,35,-78,-79,]),'FOR':([0,2,5,6,8,9,10,12,15,19,22,41,42,44,45,46,48,51,55,56,57,58,59,60,61,62,63,68,69,71,72,73,74,75,76,77,78,82,93,94,95,96,97,98,99,100,101,102,119,122,123,124,125,126,128,137,156,157,158,159,160,162,192,194,197,216,218,227,228,229,234,235,236,241,242,243,],[36,36,-20,-21,-23,-24,-25,-27,-30,-34,-76,-4,-5,-7,-8,-9,-11,-14,-18,-19,-22,-26,-28,-29,-31,-32,-33,-74,-75,-64,36,-44,36,-38,36,-41,36,-35,36,-2,-3,-6,-10,-12,-13,-15,-16,-17,-73,36,36,36,36,36,36,36,36,-67,-46,-40,-43,36,-80,-63,36,36,36,36,36,-77,36,36,-37,36,-78,-79,]),'WHILE':([0,2,5,6,8,9,10,12,15,19,22,41,42,44,45,46,48,51,55,56,57,58,59,60,61,62,63,68,69,71,72,73,74,75,76,77,78,82,93,94,95,96,97,98,99,100,101,102,119,122,123,124,125,126,128,137,156,157,158,159,160,162,192,194,197,216,218,227,228,229,234,235,236,241,242,243,],[37,37,-20,-21,-23,-24,-25,-27,-30,-34,-76,-4,-5,-7,-8,-9,-11,-14,-18,-19,-22,-26,-28,-29,-31,-32,-33,-74,-75,-64,37,-44,37,-38,37,-41,37,-35,37,-2,-3,-6,-10,-12,-13,-15,-16,-17,-73,37,37,37,37,37,37,37,37,-67,-46,-40,-43,37,-80,-63,37,37,37,37,37,-77,37,37,-37,37,-78,-79,]),'TRY':([0,2,5,6,8,9,10,12,15,19,22,41,42,44,45,46,48,51,55,56,57,58,59,60,61,62,63,68,69,71,72,73,74,75,76,77,78,82,93,94,95,96,97,98,99,100,101,102,119,122,123,124,125,126,128,137,156,157,158,159,160,162,192,194,197,216,218,227,228,229,234,235,236,241,242,243,],[38,38,-20,-21,-23,-24,-25,-27,-30,-34,-76,-4,-5,-7,-8,-9,-11,-14,-18,-19,-22,-26,-28,-29,-31,-32,-33,-74,-75,-64,38,-44,38,-38,38,-41,38,-35,38,-2,-3,-6,-10,-12,-13,-15,-16,-17,-73,38,38,38,38,38,38,38,38,-67,-46,-40,-43,38,-80,-63,38,38,38,38,38,-77,38,38,-37,38,-78,-79,]),'DOT':([0,2,5,6,8,9,10,12,15,19,21,22,31,41,42,44,45,46,48,51,55,56,57,58,59,60,61,62,63,68,69,71,72,73,74,75,76,77,78,82,93,94,95,96,97,98,99,100,101,102,110,111,112,113,114,116,117,118,119,122,123,124,125,126,128,129,137,142,148,149,152,156,157,158,159,160,162,179,180,181,182,183,185,186,192,194,196,197,212,213,216,218,227,228,229,234,235,236,237,238,239,240,241,242,243,],[32,32,-20,-21,-23,-24,-25,-27,-30,-34,67,-76,86,-4,-5,-7,-8,-9,-11,-14,-18,-19,-22,-26,-28,-29,-31,-32,-33,-74,-75,-64,32,-44,32,-38,32,-41,32,-35,32,-2,-3,-6,-10,-12,-13,-15,-16,-17,-101,-102,-103,-104,150,-71,-106,-58,-73,32,32,32,32,32,32,-50,32,-105,-98,184,187,32,-67,-46,-40,-43,32,-96,-97,-99,-100,-107,-57,-70,-80,-63,-49,32,-55,-56,32,32,32,32,-77,32,32,-37,-51,-53,-52,-54,32,-78,-79,]),'$end':([0,1,2,5,6,8,9,10,12,15,19,22,41,42,44,45,46,48,51,55,56,57,58,59,60,61,62,63,68,69,71,73,75,77,82,94,95,96,97,98,99,100,101,102,119,157,158,159,160,192,194,229,236,242,243,],[-108,0,-1,-20,-21,-23,-24,-25,-27,-30,-34,-76,-4,-5,-7,-8,-9,-11,-14,-18,-19,-22,-26,-28,-29,-31,-32,-33,-74,-75,-64,-44,-38,-41,-35,-2,-3,-6,-10,-12,-13,-15,-16,-17,-73,-67,-46,-40,-43,-80,-63,-77,-37,-78,-79,]),'SEMI':([3,4,7,11,13,14,16,17,18,21,31,39,40,43,47,49,50,52,53,54,64,79,80,81,84,105,106,107,110,111,112,113,117,118,129,139,140,142,148,149,152,175,179,180,181,182,183,185,196,208,209,212,213,217,222,223,237,238,239,240,],[55,56,57,58,59,60,61,62,63,-90,-47,94,95,96,97,98,99,100,101,102,-95,-87,-72,-88,-89,-104,-91,-92,-101,-102,-103,-104,-106,-58,-50,-104,-94,-105,-98,-68,-69,-93,-96,-97,-99,-100,-107,-57,-49,-61,-62,-55,-56,-48,-59,-60,-51,-53,-52,-54,]),'RMB':([5,6,8,9,10,12,15,19,22,41,42,44,45,46,48,51,55,56,57,58,59,60,61,62,63,68,69,71,72,73,74,75,76,77,78,82,93,94,95,96,97,98,99,100,101,102,119,122,123,124,125,126,128,137,156,157,158,159,160,162,192,194,197,216,218,227,228,229,234,235,236,241,242,243,],[-20,-21,-23,-24,-25,-27,-30,-34,-76,-4,-5,-7,-8,-9,-11,-14,-18,-19,-22,-26,-28,-29,-31,-32,-33,-74,-75,-64,-108,-44,-108,-38,-108,-41,-108,-35,-108,-2,-3,-6,-10,-12,-13,-15,-16,-17,-73,-108,157,158,159,160,-108,174,192,-67,-46,-40,-43,194,-80,-63,-108,-108,229,-108,236,-77,-108,242,-37,243,-78,-79,]),'EQUAL':([21,64,103,110,111,112,113,117,131,132,136,142,148,166,167,179,180,181,182,183,191,198,200,202,214,219,220,],[65,104,138,-101,-102,-103,-104,-106,168,-86,168,-105,-98,199,201,-96,-97,-99,-100,-107,168,-81,-82,-85,168,-83,-84,]),'LSB':([21,33,35,36,37,65,66,83,87,88,89,90,92,104,105,108,109,118,121,129,133,138,139,141,143,144,145,146,151,153,154,155,163,166,167,168,176,190,199,201,210,211,224,225,],[66,88,90,91,92,108,108,127,130,108,133,108,108,108,141,108,108,153,155,163,108,108,176,108,108,108,108,108,108,108,190,108,108,108,108,108,108,108,108,108,224,225,108,108,]),'ELSE':([22,68,229,242,243,],[70,120,-77,-78,-79,]),'LMB':([23,24,25,26,38,70,85,120,165,171,173,193,203,204,215,221,226,],[72,74,76,78,93,122,128,122,197,-45,-42,216,-65,-66,227,-39,234,]),'DEBUG':([27,],[80,]),'CATCH':([28,174,],[83,-36,]),'LIST':([64,65,66,88,90,92,104,105,108,109,113,133,138,139,141,143,144,145,146,151,153,155,163,166,167,168,176,190,199,201,224,225,],[103,106,117,117,117,117,117,142,117,117,142,117,117,142,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,]),'MINUS':([65,66,88,90,92,104,105,106,107,108,109,110,111,112,113,116,117,132,133,134,138,139,140,141,142,143,144,145,146,147,148,151,153,155,163,166,167,168,175,176,179,180,181,182,183,186,190,198,199,200,201,202,219,220,224,225,],[109,109,109,109,109,109,-104,-106,144,109,109,-101,-102,-103,-104,144,-106,144,109,144,109,-104,144,109,-105,109,109,109,109,144,-98,109,109,109,109,109,109,109,144,109,-96,-97,-99,-100,-107,144,109,144,109,144,109,144,144,144,109,109,]),'INT':([65,66,88,90,92,104,108,109,133,138,141,143,144,145,146,151,153,155,163,166,167,168,176,190,199,201,224,225,],[110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,]),'FLOAT':([65,66,88,90,92,104,108,109,133,138,141,143,144,145,146,151,153,155,163,166,167,168,176,190,199,201,224,225,],[111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,]),'STRING':([65,66,88,90,92,104,108,109,133,138,141,143,144,145,146,151,153,155,163,166,167,168,176,190,199,201,224,225,],[112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,]),'RSB':([66,110,111,112,113,114,115,116,117,130,131,132,133,134,136,141,142,147,148,153,161,164,169,170,176,177,178,179,180,181,182,183,186,188,189,191,195,198,200,202,205,206,207,214,219,220,224,225,230,231,232,233,],[-108,-101,-102,-103,-104,149,152,-71,-106,-108,165,-86,-108,171,173,-108,-105,183,-98,-108,193,196,203,204,-108,208,209,-96,-97,-99,-100,-107,-70,212,213,215,217,-81,-82,-85,221,222,223,226,-83,-84,-108,-108,237,238,239,240,]),'PLUS':([105,106,107,110,111,112,113,116,117,132,134,139,140,142,147,148,175,179,180,181,182,183,186,198,200,202,219,220,],[-104,-106,143,-101,-102,-103,-104,143,-106,143,143,-104,143,-105,143,-98,143,-96,-97,-99,-100,-107,143,143,143,143,143,143,]),'MUL':([105,106,107,110,111,112,113,116,117,132,134,139,140,142,147,148,175,179,180,181,182,183,186,198,200,202,219,220,],[-104,-106,145,-101,-102,-103,-104,145,-106,145,145,-104,145,-105,145,-98,145,145,145,-99,-100,-107,145,145,145,145,145,145,]),'DIV':([105,106,107,110,111,112,113,116,117,132,134,139,140,142,147,148,175,179,180,181,182,183,186,198,200,202,219,220,],[-104,-106,146,-101,-102,-103,-104,146,-106,146,146,-104,146,-105,146,-98,146,146,146,-99,-100,-107,146,146,146,146,146,146,]),'COMMA':([110,111,112,113,114,116,117,142,148,169,177,179,180,181,182,183,186,188,195,206,230,233,],[-101,-102,-103,-104,151,-71,-106,-105,-98,151,151,-96,-97,-99,-100,-107,-70,151,151,151,151,151,]),'LB':([110,111,112,113,117,131,132,136,142,148,179,180,181,182,183,191,198,200,202,214,219,220,],[-101,-102,-103,-104,-106,166,-86,166,-105,-98,-96,-97,-99,-100,-107,166,-81,-82,-85,166,-83,-84,]),'RB':([110,111,112,113,117,131,132,136,142,148,179,180,181,182,183,191,198,200,202,214,219,220,],[-101,-102,-103,-104,-106,167,-86,167,-105,-98,-96,-97,-99,-100,-107,167,-81,-82,-85,167,-83,-84,]),'IN':([135,],[172,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'root':([0,],[1,]),'expression':([0,72,74,76,78,93,122,128,197,216,227,234,],[2,123,124,125,126,137,156,162,218,228,235,241,]),'variable_declaration':([0,2,72,74,76,78,93,122,123,124,125,126,128,137,156,162,197,216,218,227,228,234,235,241,],[3,39,3,3,3,3,3,3,39,39,39,39,3,39,39,39,3,3,39,3,39,3,39,39,]),'variable_value_change':([0,2,72,74,76,78,93,122,123,124,125,126,128,137,156,162,197,216,218,227,228,234,235,241,],[4,40,4,4,4,4,4,4,40,40,40,40,4,40,40,40,4,4,40,4,40,4,40,40,]),'if_statement':([0,2,72,74,76,78,93,122,123,124,125,126,128,137,156,162,197,216,218,227,228,234,235,241,],[5,41,5,5,5,5,5,5,41,41,41,41,5,41,41,41,5,5,41,5,41,5,41,41,]),'function':([0,2,72,74,76,78,93,122,123,124,125,126,128,137,156,162,197,216,218,227,228,234,235,241,],[6,42,6,6,6,6,6,6,42,42,42,42,6,42,42,42,6,6,42,6,42,6,42,42,]),'function_call':([0,2,72,74,76,78,93,122,123,124,125,126,128,137,156,162,197,216,218,227,228,234,235,241,],[7,43,7,7,7,7,7,7,43,43,43,43,7,43,43,43,7,7,43,7,43,7,43,43,]),'repeat':([0,2,72,74,76,78,93,122,123,124,125,126,128,137,156,162,197,216,218,227,228,234,235,241,],[8,44,8,8,8,8,8,8,44,44,44,44,8,44,44,44,8,8,44,8,44,8,44,44,]),'for':([0,2,72,74,76,78,93,122,123,124,125,126,128,137,156,162,197,216,218,227,228,234,235,241,],[9,45,9,9,9,9,9,9,45,45,45,45,9,45,45,45,9,9,45,9,45,9,45,45,]),'while':([0,2,72,74,76,78,93,122,123,124,125,126,128,137,156,162,197,216,218,227,228,234,235,241,],[10,46,10,10,10,10,10,10,46,46,46,46,10,46,46,46,10,10,46,10,46,10,46,46,]),'use':([0,2,72,74,76,78,93,122,123,124,125,126,128,137,156,162,197,216,218,227,228,234,235,241,],[11,47,11,11,11,11,11,11,47,47,47,47,11,47,47,47,11,11,47,11,47,11,47,47,]),'error_handling':([0,2,72,74,76,78,93,122,123,124,125,126,128,137,156,162,197,216,218,227,228,234,235,241,],[12,48,12,12,12,12,12,12,48,48,48,48,12,48,48,48,12,12,48,12,48,12,48,48,]),'variable_alone':([0,2,72,74,76,78,93,122,123,124,125,126,128,137,156,162,197,216,218,227,228,234,235,241,],[13,49,13,13,13,13,13,13,49,49,49,49,13,49,49,49,13,13,49,13,49,13,49,49,]),'global_variable':([0,2,72,74,76,78,93,122,123,124,125,126,128,137,156,162,197,216,218,227,228,234,235,241,],[14,50,14,14,14,14,14,14,50,50,50,50,14,50,50,50,14,14,50,14,50,14,50,50,]),'class_def':([0,2,72,74,76,78,93,122,123,124,125,126,128,137,156,162,197,216,218,227,228,234,235,241,],[15,51,15,15,15,15,15,15,51,51,51,51,15,51,51,51,15,15,51,15,51,15,51,51,]),'debug':([0,2,72,74,76,78,93,122,123,124,125,126,128,137,156,162,197,216,218,227,228,234,235,241,],[16,52,16,16,16,16,16,16,52,52,52,52,16,52,52,52,16,16,52,16,52,16,52,52,]),'function_class':([0,2,72,74,76,78,93,122,123,124,125,126,128,137,156,162,197,216,218,227,228,234,235,241,],[17,53,17,17,17,17,17,17,53,53,53,53,17,53,53,53,17,17,53,17,53,17,53,53,]),'inside_root':([0,2,72,74,76,78,93,122,123,124,125,126,128,137,156,162,197,216,218,227,228,234,235,241,],[18,54,18,18,18,18,18,18,54,54,54,54,18,54,54,54,18,18,54,18,54,18,54,54,]),'empty':([0,66,72,74,76,78,93,122,128,130,133,141,153,176,197,216,224,225,227,234,],[19,115,19,19,19,19,19,19,19,164,170,178,189,207,19,19,231,232,19,19,]),'if_statement_1':([0,2,72,74,76,78,93,122,123,124,125,126,128,137,156,162,197,216,218,227,228,234,235,241,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'function_head':([0,2,72,74,76,78,93,122,123,124,125,126,128,137,156,162,197,216,218,227,228,234,235,241,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'repeat_head':([0,2,72,74,76,78,93,122,123,124,125,126,128,137,156,162,197,216,218,227,228,234,235,241,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'for_head':([0,2,72,74,76,78,93,122,123,124,125,126,128,137,156,162,197,216,218,227,228,234,235,241,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'while_head':([0,2,72,74,76,78,93,122,123,124,125,126,128,137,156,162,197,216,218,227,228,234,235,241,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'try':([0,2,72,74,76,78,93,122,123,124,125,126,128,137,156,162,197,216,218,227,228,234,235,241,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'inside':([0,2,72,74,76,78,93,122,123,124,125,126,128,137,156,162,197,216,218,227,228,234,235,241,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'if_statement_2':([22,],[68,]),'if_statement_3':([22,68,],[69,119,]),'function_body':([23,],[71,]),'repeat_body':([24,],[73,]),'for_body':([25,],[75,]),'while_body':([26,],[77,]),'use_params':([27,],[79,]),'catch':([28,],[82,]),'calculate':([65,66,88,90,92,104,108,109,133,138,141,143,144,145,146,151,153,155,163,166,167,168,176,190,199,201,224,225,],[107,116,132,134,132,140,147,148,116,175,116,179,180,181,182,186,116,132,116,198,200,202,116,132,219,220,116,116,]),'parameter':([66,133,141,153,163,176,224,225,],[114,169,177,188,195,206,230,233,]),'condition':([88,92,155,190,],[131,136,191,214,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> root","S'",1,None,None,None),
  ('root -> expression','root',1,'p_root','main.py',157),
  ('expression -> expression variable_declaration SEMI','expression',3,'p_expression_variable','main.py',191),
  ('expression -> expression variable_value_change SEMI','expression',3,'p_expression_variable','main.py',192),
  ('expression -> expression if_statement','expression',2,'p_expression_if_statement','main.py',209),
  ('expression -> expression function','expression',2,'p_expression_function','main.py',220),
  ('expression -> expression function_call SEMI','expression',3,'p_expression_function_call','main.py',226),
  ('expression -> expression repeat','expression',2,'p_expression_repeat','main.py',232),
  ('expression -> expression for','expression',2,'p_expression_for','main.py',238),
  ('expression -> expression while','expression',2,'p_expression_while','main.py',244),
  ('expression -> expression use SEMI','expression',3,'p_expression_use','main.py',250),
  ('expression -> expression error_handling','expression',2,'p_expression_error_handling','main.py',256),
  ('expression -> expression variable_alone SEMI','expression',3,'p_expression_variable_alone','main.py',262),
  ('expression -> expression global_variable SEMI','expression',3,'p_expression_global_variable','main.py',268),
  ('expression -> expression class_def','expression',2,'p_expression_class_def','main.py',274),
  ('expression -> expression debug SEMI','expression',3,'p_expression_debug','main.py',280),
  ('expression -> expression function_class SEMI','expression',3,'p_expression_function_class','main.py',286),
  ('expression -> expression inside_root SEMI','expression',3,'p_expression_inside','main.py',292),
  ('expression -> variable_declaration SEMI','expression',2,'p_expression_variable_2','main.py',300),
  ('expression -> variable_value_change SEMI','expression',2,'p_expression_variable_2','main.py',301),
  ('expression -> if_statement','expression',1,'p_expression_if_statement_2','main.py',312),
  ('expression -> function','expression',1,'p_expression_function_2','main.py',320),
  ('expression -> function_call SEMI','expression',2,'p_expression_function_call_2','main.py',326),
  ('expression -> repeat','expression',1,'p_expression_repeat_2','main.py',332),
  ('expression -> for','expression',1,'p_expression_for_2','main.py',338),
  ('expression -> while','expression',1,'p_expression_while_2','main.py',344),
  ('expression -> use SEMI','expression',2,'p_expression_use_2','main.py',350),
  ('expression -> error_handling','expression',1,'p_expression_error_handling_2','main.py',356),
  ('expression -> variable_alone SEMI','expression',2,'p_expression_variable_alone_2','main.py',362),
  ('expression -> global_variable SEMI','expression',2,'p_expression_global_variable_2','main.py',368),
  ('expression -> class_def','expression',1,'p_expression_class_def_2','main.py',374),
  ('expression -> debug SEMI','expression',2,'p_expression_debug_2','main.py',380),
  ('expression -> function_class SEMI','expression',2,'p_expression_function_class_2','main.py',386),
  ('expression -> inside_root SEMI','expression',2,'p_expression_inside_2','main.py',392),
  ('expression -> empty','expression',1,'p_expression_empty','main.py',400),
  ('error_handling -> try catch','error_handling',2,'p_error_handling','main.py',409),
  ('try -> TRY LMB expression RMB','try',4,'p_try','main.py',415),
  ('catch -> CATCH LSB IDENTIFIER RSB LMB expression RMB','catch',7,'p_catch','main.py',426),
  ('for -> for_head for_body','for',2,'p_for','main.py',439),
  ('for_head -> FOR LSB IDENTIFIER IN IDENTIFIER RSB','for_head',6,'p_for_head','main.py',447),
  ('for_body -> LMB expression RMB','for_body',3,'p_for_body','main.py',453),
  ('while -> while_head while_body','while',2,'p_while','main.py',464),
  ('while_head -> WHILE LSB condition RSB','while_head',4,'p_while_head','main.py',472),
  ('while_body -> LMB expression RMB','while_body',3,'p_while_body','main.py',478),
  ('repeat -> repeat_head repeat_body','repeat',2,'p_repeat','main.py',490),
  ('repeat_head -> REPEAT LSB calculate RSB','repeat_head',4,'p_repeat_head','main.py',498),
  ('repeat_body -> LMB expression RMB','repeat_body',3,'p_repeat_body','main.py',504),
  ('inside_root -> inside','inside_root',1,'p_inside_root_1','main.py',515),
  ('inside_root -> inside DOT IDENTIFIER LSB parameter RSB','inside_root',6,'p_inside_root_2','main.py',521),
  ('inside -> DOT IDENTIFIER LSB empty RSB','inside',5,'p_inside_root_3','main.py',527),
  ('inside -> inside DOT IDENTIFIER','inside',3,'p_inside_root_4','main.py',533),
  ('inside -> IDENTIFIER LSB parameter RSB DOT IDENTIFIER LSB parameter RSB','inside',9,'p_inside_1_1','main.py',539),
  ('inside -> IDENTIFIER LSB empty RSB DOT IDENTIFIER LSB empty RSB','inside',9,'p_inside_1_2','main.py',545),
  ('inside -> IDENTIFIER LSB parameter RSB DOT IDENTIFIER LSB empty RSB','inside',9,'p_inside_1_3','main.py',551),
  ('inside -> IDENTIFIER LSB empty RSB DOT IDENTIFIER LSB parameter RSB','inside',9,'p_inside_1_4','main.py',557),
  ('inside -> IDENTIFIER DOT IDENTIFIER LSB parameter RSB','inside',6,'p_inside_2_1','main.py',563),
  ('inside -> IDENTIFIER DOT IDENTIFIER LSB empty RSB','inside',6,'p_inside_2_2','main.py',569),
  ('inside -> IDENTIFIER LSB parameter DOT IDENTIFIER','inside',5,'p_inside_3','main.py',575),
  ('inside -> IDENTIFIER DOT IDENTIFIER','inside',3,'p_inside_4','main.py',581),
  ('function_class -> VAR IDENTIFIER EQUAL IDENTIFIER LSB parameter RSB','function_class',7,'p_function_class_declaration','main.py',589),
  ('function_class -> VAR IDENTIFIER EQUAL IDENTIFIER LSB empty RSB','function_class',7,'p_function_class_declaration','main.py',590),
  ('function_class -> IDENTIFIER EQUAL IDENTIFIER LSB parameter RSB','function_class',6,'p_function_class_call','main.py',599),
  ('function_class -> IDENTIFIER EQUAL IDENTIFIER LSB empty RSB','function_class',6,'p_function_class_call','main.py',600),
  ('class_def -> CLASS IDENTIFIER LMB expression RMB','class_def',5,'p_class_def','main.py',611),
  ('function -> function_head function_body','function',2,'p_function','main.py',626),
  ('function_head -> FUNCTION IDENTIFIER LSB parameter RSB','function_head',5,'p_function_head','main.py',634),
  ('function_head -> FUNCTION IDENTIFIER LSB empty RSB','function_head',5,'p_function_head','main.py',635),
  ('function_body -> LMB expression RMB','function_body',3,'p_function_body','main.py',644),
  ('function_call -> IDENTIFIER LSB parameter RSB','function_call',4,'p_function_call','main.py',655),
  ('function_call -> IDENTIFIER LSB empty RSB','function_call',4,'p_function_call','main.py',656),
  ('parameter -> parameter COMMA calculate','parameter',3,'p_parameter','main.py',667),
  ('parameter -> calculate','parameter',1,'p_parameter_2','main.py',673),
  ('debug -> USE DEBUG','debug',2,'p_debug','main.py',685),
  ('if_statement -> if_statement_1 if_statement_2 if_statement_3','if_statement',3,'p_if_statement','main.py',695),
  ('if_statement -> if_statement_1 if_statement_2','if_statement',2,'p_if_statement','main.py',696),
  ('if_statement -> if_statement_1 if_statement_3','if_statement',2,'p_if_statement','main.py',697),
  ('if_statement -> if_statement_1','if_statement',1,'p_if_statement','main.py',698),
  ('if_statement_1 -> IF LSB condition RSB LMB expression RMB','if_statement_1',7,'p_if_statement_1','main.py',710),
  ('if_statement_2 -> ELSE IF LSB condition RSB LMB expression RMB','if_statement_2',8,'p_if_statement_2','main.py',719),
  ('if_statement_2 -> if_statement_2 ELSE IF LSB condition RSB LMB expression RMB','if_statement_2',9,'p_if_statement_2_2','main.py',730),
  ('if_statement_3 -> ELSE LMB expression RMB','if_statement_3',4,'p_if_statement_3','main.py',741),
  ('condition -> condition LB calculate','condition',3,'p_condition','main.py',754),
  ('condition -> condition RB calculate','condition',3,'p_condition','main.py',755),
  ('condition -> condition LB EQUAL calculate','condition',4,'p_condition_2','main.py',761),
  ('condition -> condition RB EQUAL calculate','condition',4,'p_condition_2','main.py',762),
  ('condition -> condition EQUAL calculate','condition',3,'p_condition_3','main.py',768),
  ('condition -> calculate','condition',1,'p_condition_4','main.py',774),
  ('use -> USE use_params','use',2,'p_use','main.py',782),
  ('use_params -> IDENTIFIER','use_params',1,'p_use_params','main.py',807),
  ('global_variable -> GLOBAL IDENTIFIER','global_variable',2,'p_global_variable','main.py',814),
  ('variable_alone -> IDENTIFIER','variable_alone',1,'p_variable_alone','main.py',822),
  ('variable_value_change -> IDENTIFIER EQUAL LIST','variable_value_change',3,'p_variable_value_change_list','main.py',830),
  ('variable_value_change -> IDENTIFIER EQUAL calculate','variable_value_change',3,'p_variable_value_change','main.py',836),
  ('variable_declaration -> VAR IDENTIFIER LIST EQUAL calculate','variable_declaration',5,'p_variable_declaration_list','main.py',864),
  ('variable_declaration -> VAR IDENTIFIER EQUAL calculate','variable_declaration',4,'p_variable_declaration_2','main.py',870),
  ('variable_declaration -> VAR IDENTIFIER','variable_declaration',2,'p_variable_declaration_1','main.py',886),
  ('calculate -> calculate PLUS calculate','calculate',3,'p_add','main.py',915),
  ('calculate -> calculate MINUS calculate','calculate',3,'p_sub','main.py',951),
  ('calculate -> MINUS calculate','calculate',2,'p_calculate2uminus','main.py',955),
  ('calculate -> calculate MUL calculate','calculate',3,'p_mul_div','main.py',960),
  ('calculate -> calculate DIV calculate','calculate',3,'p_mul_div','main.py',961),
  ('calculate -> INT','calculate',1,'p_calculate2num','main.py',972),
  ('calculate -> FLOAT','calculate',1,'p_calculate2num','main.py',973),
  ('calculate -> STRING','calculate',1,'p_calculate2num','main.py',974),
  ('calculate -> IDENTIFIER','calculate',1,'p_calculate2str','main.py',980),
  ('calculate -> IDENTIFIER LIST','calculate',2,'p_calculate2list','main.py',989),
  ('calculate -> LIST','calculate',1,'p_calculate2list_2','main.py',995),
  ('calculate -> LSB calculate RSB','calculate',3,'p_parens','main.py',1000),
  ('empty -> <empty>','empty',0,'p_empty','main.py',1006),
]
