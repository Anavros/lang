
import lang
import lang.objects as o


def _is_empty_program(p):
    return isinstance(p, o.Program) and p.statements == []


def test_empty_program():
    """
    Empty sources should produce Program() objects with empty statement lists,
    not None objects.
    """
    source = ""
    program = lang.ast(source)
    assert _is_empty_program(program)


def test_comment_emptiness():
    source = """
    # Are comments ignored?
    """
    program = lang.ast(source)
    assert _is_empty_program(program)
