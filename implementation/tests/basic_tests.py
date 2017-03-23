
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


def test_empty_return():
    source = """
    return();
    """
    result = lang.run(source)
    assert result == []


def test_value_return():
    source = """
    return("Hello");
    """
    result = lang.run(source)
    assert result == [(0, "Hello")]


def test_function_result_return():
    source = """
    return(sum(2, 2));
    """
    program = lang.run(source)
    assert program == [(0, 4)]


def test_nested_result_return():
    source = """
    return(sum(2, sum(2, 2)));
    """
    program = lang.run(source)
    assert program == [(0, 6)]


def test_named_arg_return():
    source = """
    return(x = 1);
    """
    program = lang.run(source)
    assert program == [('x', 1)]


def test_variable_assignment():
    source = """
    assign("x", 10);
    return(x);
    """
    # It tries to return [('x', 10)] because 'x' has a name.
    # This probably isn't what we want?
    program = lang.run(source)
    assert program == [(0, 10)]


def _test_function_creation():
    source = """
    function("four", (), {
        return(4);
    });
    return(four());
    """
    # Just make sure it doesn't throw any errors.
    result = lang.run(source)
    assert result == [(0, 4)];


def _test_function_argument_passing():
    source = """
    function("echo", (x), {
        return(x);
    });
    return(echo("Hello"));
    """
    result = lang.run(source)
    assert result == [(0, "Hello")]
