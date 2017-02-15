
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'LPAREN RPAREN ASSIGN SEMICOLON COMMA COLON NUMERAL STRING NAME\n    program : program statement\n    \n    program : statement\n    \n    statement : function_call SEMICOLON\n              | assignment SEMICOLON\n    \n    function_call : NAME LPAREN argument_list RPAREN\n    \n    argument : value\n    \n    argument_list : argument_list COMMA argument\n    \n    argument_list : argument\n    \n    assignment : variable ASSIGN value\n    \n    variable : NAME\n    \n    value : variable\n          | constant\n    \n    constant : STRING\n             | NUMERAL\n    '
    
_lr_action_items = {'ASSIGN':([2,5,],[-10,10,]),'RPAREN':([12,13,14,15,16,17,18,19,23,],[-14,-11,-13,22,-6,-10,-12,-8,-7,]),'LPAREN':([2,],[7,]),'STRING':([7,10,21,],[14,14,14,]),'COMMA':([12,13,14,15,16,17,18,19,23,],[-14,-11,-13,21,-6,-10,-12,-8,-7,]),'NAME':([0,1,3,7,8,9,10,11,21,],[2,-2,2,17,-1,-3,17,-4,17,]),'NUMERAL':([7,10,21,],[12,12,12,]),'$end':([1,3,8,9,11,],[-2,0,-1,-3,-4,]),'SEMICOLON':([4,6,12,13,14,17,18,20,22,],[9,11,-14,-11,-13,-10,-12,-9,-5,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'function_call':([0,3,],[4,4,]),'variable':([0,3,7,10,21,],[5,5,13,13,13,]),'assignment':([0,3,],[6,6,]),'statement':([0,3,],[1,8,]),'argument_list':([7,],[15,]),'value':([7,10,21,],[16,20,16,]),'constant':([7,10,21,],[18,18,18,]),'program':([0,],[3,]),'argument':([7,21,],[19,23,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> program statement','program',2,'p_program','yacker.py',9),
  ('program -> statement','program',1,'p_program_end','yacker.py',17),
  ('statement -> function_call SEMICOLON','statement',2,'p_statement','yacker.py',24),
  ('statement -> assignment SEMICOLON','statement',2,'p_statement','yacker.py',25),
  ('function_call -> NAME LPAREN argument_list RPAREN','function_call',4,'p_function_call','yacker.py',32),
  ('argument -> value','argument',1,'p_argument','yacker.py',39),
  ('argument_list -> argument_list COMMA argument','argument_list',3,'p_argument_list','yacker.py',46),
  ('argument_list -> argument','argument_list',1,'p_argument_list_terminal','yacker.py',54),
  ('assignment -> variable ASSIGN value','assignment',3,'p_assignment','yacker.py',61),
  ('variable -> NAME','variable',1,'p_variable','yacker.py',68),
  ('value -> variable','value',1,'p_value','yacker.py',75),
  ('value -> constant','value',1,'p_value','yacker.py',76),
  ('constant -> STRING','constant',1,'p_constant','yacker.py',83),
  ('constant -> NUMERAL','constant',1,'p_constant','yacker.py',84),
]
