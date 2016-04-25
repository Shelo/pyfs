from tests.testengine import TestEngine
import pyfs


def test_vim():
    pyfs.prompt.vim("testdir/file1.md")


def test_confirm():
    value = pyfs.prompt.confirm("Say yes: ")
    assert value is True

test_engine = TestEngine(__name__)
