
import lang
import lang.objects as o


def test_empty_program():
    """
    Empty sources should produce Program() objects with empty statement lists,
    not None objects.
    """
    source = ""
    program = lang.ast(source)
    assert isinstance(program, o.Program)
    assert program.statements == []


def test_comment_emptiness():
    source = """
    # Do comments work?
    """
    program = lang.ast(source)
    assert isinstance(program, o.Program)
    assert program.statements == []
