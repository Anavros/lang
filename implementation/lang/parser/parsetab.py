
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'RETURN DEFINE LPAREN RPAREN LBRACE RBRACE ASSIGN SEMICOLON COMMA COLON NUMERAL STRING NAME\n    program : program statement\n    \n    program : return SEMICOLON\n    \n    statement : call SEMICOLON\n    statement : definition SEMICOLON\n    \n    return : RETURN value\n    \n    definition : DEFINE NAME value\n    \n    definition : DEFINE NAME tuple block\n    \n    call : NAME tuple\n    \n    tuple : LPAREN arguments RPAREN\n    \n    tuple : LPAREN RPAREN\n    \n    arguments : arg\n    \n    arguments : arguments COMMA arg\n    \n    arg : positional_value\n        | named_value\n        | variable\n    \n    named_value : NAME ASSIGN value\n    \n    positional_value : value\n    \n    value : constant\n          | block\n          | call\n          | tuple\n    \n    variable : NAME\n    \n    constant : STRING\n             | NUMERAL\n    \n    block : LBRACE program RBRACE\n    '
    
_lr_action_items = {'COMMA':([10,11,12,13,17,18,20,24,25,26,27,28,29,30,31,34,36,39,40,],[-21,-18,-19,-23,-24,-20,-8,-10,-17,-15,-14,-11,-13,-22,37,-25,-9,-16,-12,]),'RPAREN':([10,11,12,13,16,17,18,20,24,25,26,27,28,29,30,31,34,36,39,40,],[-21,-18,-19,-23,24,-24,-20,-8,-10,-17,-15,-14,-11,-13,-22,36,-25,-9,-16,-12,]),'STRING':([3,16,22,35,37,],[13,13,13,13,13,]),'LBRACE':([3,16,22,24,32,35,36,37,],[14,14,14,-10,14,14,-9,14,]),'ASSIGN':([30,],[35,]),'NUMERAL':([3,16,22,35,37,],[17,17,17,17,17,]),'DEFINE':([2,4,7,19,21,23,],[9,-2,-1,-3,-4,9,]),'SEMICOLON':([1,5,8,10,11,12,13,15,17,18,20,24,32,33,34,36,38,],[4,19,21,-21,-18,-19,-23,-5,-24,-20,-8,-10,-21,-6,-25,-9,-7,]),'LPAREN':([3,6,16,22,30,35,37,],[16,16,16,16,16,16,16,]),'NAME':([2,3,4,7,9,16,19,21,22,23,35,37,],[6,6,-2,-1,22,30,-3,-4,6,6,6,30,]),'RETURN':([0,14,],[3,3,]),'$end':([2,4,7,19,21,],[0,-2,-1,-3,-4,]),'RBRACE':([4,7,19,21,23,],[-2,-1,-3,-4,34,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'tuple':([3,6,16,22,30,35,37,],[10,20,10,32,20,10,10,]),'constant':([3,16,22,35,37,],[11,11,11,11,11,]),'call':([2,3,16,22,23,35,37,],[5,18,18,18,5,18,18,]),'program':([0,14,],[2,23,]),'positional_value':([16,37,],[29,29,]),'block':([3,16,22,32,35,37,],[12,12,12,38,12,12,]),'variable':([16,37,],[26,26,]),'named_value':([16,37,],[27,27,]),'arg':([16,37,],[28,40,]),'return':([0,14,],[1,1,]),'value':([3,16,22,35,37,],[15,25,33,39,25,]),'arguments':([16,],[31,]),'statement':([2,23,],[7,7,]),'definition':([2,23,],[8,8,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> program statement','program',2,'p_program','yacker.py',10),
  ('program -> return SEMICOLON','program',2,'p_program_end','yacker.py',18),
  ('statement -> call SEMICOLON','statement',2,'p_statement','yacker.py',25),
  ('statement -> definition SEMICOLON','statement',2,'p_statement','yacker.py',26),
  ('return -> RETURN value','return',2,'p_return','yacker.py',33),
  ('definition -> DEFINE NAME value','definition',3,'p_definition','yacker.py',40),
  ('definition -> DEFINE NAME tuple block','definition',4,'p_function_definition','yacker.py',47),
  ('call -> NAME tuple','call',2,'p_call','yacker.py',54),
  ('tuple -> LPAREN arguments RPAREN','tuple',3,'p_tuple','yacker.py',61),
  ('tuple -> LPAREN RPAREN','tuple',2,'p_tuple_empty','yacker.py',68),
  ('arguments -> arg','arguments',1,'p_arguments_single','yacker.py',75),
  ('arguments -> arguments COMMA arg','arguments',3,'p_arguments_list','yacker.py',82),
  ('arg -> positional_value','arg',1,'p_arg','yacker.py',90),
  ('arg -> named_value','arg',1,'p_arg','yacker.py',91),
  ('arg -> variable','arg',1,'p_arg','yacker.py',92),
  ('named_value -> NAME ASSIGN value','named_value',3,'p_named_value','yacker.py',98),
  ('positional_value -> value','positional_value',1,'p_positional_value','yacker.py',105),
  ('value -> constant','value',1,'p_value','yacker.py',111),
  ('value -> block','value',1,'p_value','yacker.py',112),
  ('value -> call','value',1,'p_value','yacker.py',113),
  ('value -> tuple','value',1,'p_value','yacker.py',114),
  ('variable -> NAME','variable',1,'p_variable','yacker.py',120),
  ('constant -> STRING','constant',1,'p_constant','yacker.py',127),
  ('constant -> NUMERAL','constant',1,'p_constant','yacker.py',128),
  ('block -> LBRACE program RBRACE','block',3,'p_block','yacker.py',135),
]
