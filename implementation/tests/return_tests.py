
import lang


def test_empty_return():
    source = """
    return();
    """
    result = lang.run(source)
    #assert result == None
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
    # It returns [(0, [(0, 4)])].
    # So arguments are getting nested, which kind of makes sense.
    # But obviously that isn't what we want.
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
