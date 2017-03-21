
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'LPAREN RPAREN LBRACE RBRACE ASSIGN SEMICOLON COMMA COLON NUMERAL STRING NAME\n    program : program statement\n    \n    program : statement\n    \n    statement : call SEMICOLON\n    \n    block : LBRACE program RBRACE\n    \n    call : NAME tuple\n    \n    arguments : arg\n    \n    arguments : arguments COMMA arg\n    \n    arg : value\n        | pair\n    \n    pair : variable ASSIGN value\n    \n    value : variable\n          | constant\n          | block\n          | call\n          | tuple\n    \n    tuple : LPAREN arguments RPAREN\n    \n    tuple : LPAREN RPAREN\n    \n    variable : NAME\n    \n    constant : STRING\n             | NUMERAL\n    '
    
_lr_action_items = {'STRING':([7,23,25,],[17,17,17,]),'NAME':([0,1,2,5,6,7,15,23,25,26,],[4,4,-2,-1,-3,10,4,10,10,4,]),'RPAREN':([7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,24,27,28,29,30,],[19,-5,-8,-18,24,-11,-14,-6,-9,-19,-12,-17,-15,-13,-20,-16,-7,-10,-11,-4,]),'NUMERAL':([7,23,25,],[22,22,22,]),'LBRACE':([7,23,25,],[15,15,15,]),'ASSIGN':([10,12,],[-18,25,]),'LPAREN':([4,7,10,23,25,],[7,7,7,7,7,]),'$end':([1,2,5,6,],[0,-2,-1,-3,]),'RBRACE':([2,5,6,26,],[-2,-1,-3,30,]),'COMMA':([8,9,10,11,12,13,14,16,17,18,19,20,21,22,24,27,28,29,30,],[-5,-8,-18,23,-11,-14,-6,-9,-19,-12,-17,-15,-13,-20,-16,-7,-10,-11,-4,]),'SEMICOLON':([3,8,19,24,],[6,-5,-17,-16,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'value':([7,23,25,],[9,9,28,]),'constant':([7,23,25,],[18,18,18,]),'program':([0,15,],[1,26,]),'statement':([0,1,15,26,],[2,5,2,5,]),'arguments':([7,],[11,]),'tuple':([4,7,10,23,25,],[8,20,8,20,20,]),'variable':([7,23,25,],[12,12,29,]),'call':([0,1,7,15,23,25,26,],[3,3,13,3,13,13,3,]),'block':([7,23,25,],[21,21,21,]),'arg':([7,23,],[14,27,]),'pair':([7,23,],[16,16,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> program statement','program',2,'p_program','yacker.py',10),
  ('program -> statement','program',1,'p_program_end','yacker.py',18),
  ('statement -> call SEMICOLON','statement',2,'p_statement','yacker.py',25),
  ('block -> LBRACE program RBRACE','block',3,'p_block','yacker.py',32),
  ('call -> NAME tuple','call',2,'p_call','yacker.py',39),
  ('arguments -> arg','arguments',1,'p_arguments_single','yacker.py',46),
  ('arguments -> arguments COMMA arg','arguments',3,'p_arguments_list','yacker.py',53),
  ('arg -> value','arg',1,'p_arg','yacker.py',61),
  ('arg -> pair','arg',1,'p_arg','yacker.py',62),
  ('pair -> variable ASSIGN value','pair',3,'p_pair','yacker.py',69),
  ('value -> variable','value',1,'p_value','yacker.py',76),
  ('value -> constant','value',1,'p_value','yacker.py',77),
  ('value -> block','value',1,'p_value','yacker.py',78),
  ('value -> call','value',1,'p_value','yacker.py',79),
  ('value -> tuple','value',1,'p_value','yacker.py',80),
  ('tuple -> LPAREN arguments RPAREN','tuple',3,'p_tuple','yacker.py',87),
  ('tuple -> LPAREN RPAREN','tuple',2,'p_tuple_empty','yacker.py',95),
  ('variable -> NAME','variable',1,'p_variable','yacker.py',102),
  ('constant -> STRING','constant',1,'p_constant','yacker.py',109),
  ('constant -> NUMERAL','constant',1,'p_constant','yacker.py',110),
]
