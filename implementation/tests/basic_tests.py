
import lang
import lang.objects as o


def test_empty_program():
    source = ""
    assert lang.evaluate(source) == None


def _test_comment_removal():
    source = """
    # Are comments ignored?
    """
    assert lang.evaluate(source) == None
