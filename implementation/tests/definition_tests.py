
import lang


def _test_basic_definition():
    source = """
    define n 2;
    return n;
    """
    assert lang.evaluate(source) == 2;
