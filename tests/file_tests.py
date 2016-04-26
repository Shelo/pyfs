from tests.testengine import TestEngine
import pyfs


def test_copy():
    pyfs.file.copy("testdir/file_copy.md", "testdir/file_copy_cp.md")

    with open("testdir/file_copy.md") as f1:
        with open("testdir/file_copy_cp.md") as f2:
            assert f1.read() == f2.read()


def test_remove():
    pyfs.file.remove("testdir/file_copy_cp.md")


def test_remove_force():
    pyfs.file.remove("testdir/no_existent.md", ignore=True)


test_engine = TestEngine(__name__)
