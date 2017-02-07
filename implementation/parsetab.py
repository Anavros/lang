
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'LPAREN RPAREN ASSIGN SEMICOLON COMMA NUMERAL STRING NAME\n    program : program SEMICOLON statement\n    \n    program : statement SEMICOLON\n    \n    statement : call\n              | assignment\n    \n    call : NAME LPAREN arguments RPAREN\n    \n    assignment : NAME ASSIGN value\n    \n    arguments : value\n    \n    arguments : arguments COMMA value\n    \n    value : NAME\n          | STRING\n          | NUMERAL\n    '
    
_lr_action_items = {'NAME':([0,6,7,8,18,],[1,10,10,1,10,]),'SEMICOLON':([2,3,4,5,9,10,13,14,15,16,17,],[8,-4,-3,9,-2,-9,-10,-11,-6,-1,-5,]),'COMMA':([10,11,12,13,14,19,],[-9,-7,18,-10,-11,-8,]),'$end':([2,3,4,9,10,13,14,15,16,17,],[0,-4,-3,-2,-9,-10,-11,-6,-1,-5,]),'RPAREN':([10,11,12,13,14,19,],[-9,-7,17,-10,-11,-8,]),'LPAREN':([1,],[6,]),'STRING':([6,7,18,],[13,13,13,]),'NUMERAL':([6,7,18,],[14,14,14,]),'ASSIGN':([1,],[7,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'value':([6,7,18,],[11,15,19,]),'program':([0,],[2,]),'assignment':([0,8,],[3,3,]),'arguments':([6,],[12,]),'call':([0,8,],[4,4,]),'statement':([0,8,],[5,16,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> program SEMICOLON statement','program',3,'p_program','yacker.py',8),
  ('program -> statement SEMICOLON','program',2,'p_program_end','yacker.py',15),
  ('statement -> call','statement',1,'p_statement','yacker.py',22),
  ('statement -> assignment','statement',1,'p_statement','yacker.py',23),
  ('call -> NAME LPAREN arguments RPAREN','call',4,'p_call','yacker.py',30),
  ('assignment -> NAME ASSIGN value','assignment',3,'p_assignment','yacker.py',38),
  ('arguments -> value','arguments',1,'p_arguments','yacker.py',45),
  ('arguments -> arguments COMMA value','arguments',3,'p_arguments_list','yacker.py',52),
  ('value -> NAME','value',1,'p_value','yacker.py',60),
  ('value -> STRING','value',1,'p_value','yacker.py',61),
  ('value -> NUMERAL','value',1,'p_value','yacker.py',62),
]
