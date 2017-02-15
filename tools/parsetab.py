
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'LPAREN RPAREN ASSIGN SEMICOLON COMMA NUMERAL STRING NAME\n    program : program statement\n    \n    program : statement\n    \n    statement : function_call SEMICOLON\n              | assignment SEMICOLON\n              | function_def SEMICOLON\n    \n    function_call : NAME LPAREN argument_list RPAREN\n    \n    argument : value\n    \n    argument_list : argument_list COMMA argument\n    \n    argument_list : argument\n    \n    function_def : NAME NAME LPAREN RPAREN\n    \n    function_def : NAME NAME LPAREN RPAREN NAME NAME\n    \n    function_def : NAME NAME LPAREN parameter_list RPAREN\n    \n    function_def : NAME NAME LPAREN parameter_list RPAREN NAME NAME\n    \n    parameter : NAME NAME\n    \n    parameter_list : parameter_list COMMA parameter\n    \n    parameter_list : parameter\n    \n    assignment : variable ASSIGN value\n    \n    value : variable\n          | constant\n    \n    variable : NAME\n    \n    constant : STRING\n             | NUMERAL\n    '
    
_lr_action_items = {'LPAREN':([4,11,],[10,23,]),'STRING':([10,14,26,],[20,20,20,]),'RPAREN':([15,16,17,18,19,20,21,22,23,27,29,31,35,37,],[-19,-22,25,-9,-7,-21,-18,-20,28,32,-16,-8,-14,-15,]),'ASSIGN':([4,7,],[-20,14,]),'COMMA':([15,16,17,18,19,20,21,22,27,29,31,35,37,],[-19,-22,26,-9,-7,-21,-18,-20,33,-16,-8,-14,-15,]),'$end':([1,2,8,9,12,13,],[-2,0,-1,-3,-5,-4,]),'NUMERAL':([10,14,26,],[16,16,16,]),'NAME':([0,1,2,4,8,9,10,12,13,14,23,26,28,30,32,33,34,36,],[4,-2,4,11,-1,-3,22,-5,-4,22,30,22,34,35,36,30,38,39,]),'SEMICOLON':([3,5,6,15,16,20,21,22,24,25,28,32,38,39,],[9,12,13,-19,-22,-21,-18,-20,-17,-6,-10,-12,-11,-13,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'constant':([10,14,26,],[15,15,15,]),'statement':([0,2,],[1,8,]),'argument_list':([10,],[17,]),'argument':([10,26,],[18,31,]),'value':([10,14,26,],[19,24,19,]),'function_call':([0,2,],[3,3,]),'variable':([0,2,10,14,26,],[7,7,21,21,21,]),'parameter':([23,33,],[29,37,]),'function_def':([0,2,],[5,5,]),'parameter_list':([23,],[27,]),'assignment':([0,2,],[6,6,]),'program':([0,],[2,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> program statement','program',2,'p_program','yacker.py',9),
  ('program -> statement','program',1,'p_program_terminal','yacker.py',17),
  ('statement -> function_call SEMICOLON','statement',2,'p_statement','yacker.py',24),
  ('statement -> assignment SEMICOLON','statement',2,'p_statement','yacker.py',25),
  ('statement -> function_def SEMICOLON','statement',2,'p_statement','yacker.py',26),
  ('function_call -> NAME LPAREN argument_list RPAREN','function_call',4,'p_function_call','yacker.py',33),
  ('argument -> value','argument',1,'p_argument','yacker.py',40),
  ('argument_list -> argument_list COMMA argument','argument_list',3,'p_argument_list','yacker.py',47),
  ('argument_list -> argument','argument_list',1,'p_argument_list_terminal','yacker.py',55),
  ('function_def -> NAME NAME LPAREN RPAREN','function_def',4,'p_function_def_nothing','yacker.py',62),
  ('function_def -> NAME NAME LPAREN RPAREN NAME NAME','function_def',6,'p_function_def_no_parameters','yacker.py',69),
  ('function_def -> NAME NAME LPAREN parameter_list RPAREN','function_def',5,'p_function_def_no_return','yacker.py',76),
  ('function_def -> NAME NAME LPAREN parameter_list RPAREN NAME NAME','function_def',7,'p_function_def','yacker.py',83),
  ('parameter -> NAME NAME','parameter',2,'p_parameter','yacker.py',90),
  ('parameter_list -> parameter_list COMMA parameter','parameter_list',3,'p_parameter_list','yacker.py',97),
  ('parameter_list -> parameter','parameter_list',1,'p_parameter_list_terminal','yacker.py',105),
  ('assignment -> variable ASSIGN value','assignment',3,'p_assignment','yacker.py',112),
  ('value -> variable','value',1,'p_value','yacker.py',119),
  ('value -> constant','value',1,'p_value','yacker.py',120),
  ('variable -> NAME','variable',1,'p_variable','yacker.py',127),
  ('constant -> STRING','constant',1,'p_constant','yacker.py',134),
  ('constant -> NUMERAL','constant',1,'p_constant','yacker.py',135),
]