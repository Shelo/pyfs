from tests.testengine import TestEngine
import pyfs


def test_copy():
    pyfs.file.copy("testdir/file1.md", "testdir/file2.md")


def test_remove():
    pyfs.file.remove("testdir/file2.md")


def test_remove_force():
    pyfs.file.remove("testdir/file2.md", ignore=True)


test_engine = TestEngine(__name__)
