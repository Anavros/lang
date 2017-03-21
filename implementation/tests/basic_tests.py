
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


def test_program_return_values():
    source = """
    return(sum(2, 2));
    """
    # NOTE: in the future, not assigning a retval might be an error.
    program = lang.run(lang.ast(source))
    assert program == [[4]]  # return vals are always lists


def test_function_creation():
    source = """
    function("four", {
        return(4);
    });

    four();
    """
    # Just make sure it doesn't throw any errors.
    result = lang.run(lang.ast(source))
