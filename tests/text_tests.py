from tests.testengine import TestEngine
import pyfs


def test_replace():
    pyfs.file.copy("testdir/text_replace.md", "testdir/text_replace_cp.md")

    pyfs.text.replace("testdir/text_replace_cp.md", (
        ('example.com', 'test.com'),
        ('example', 'Test'),
        ('name', 'Test Project')
    ))

    with open("testdir/text_replace_cp.md") as f:
        assert f.read() == 'test.com:1\n' \
                           'Test:2\n' \
                           'test.com:3\n' \
                           'Test Project:4\n' \
                           'Test:5'

    pyfs.file.remove("testdir/text_replace_cp.md")


def test_contains():
    assert pyfs.text.contains("testdir/text_contains.md", "test") == True


test_engine = TestEngine(__name__)
