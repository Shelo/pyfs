from tests.testengine import TestEngine
import pyfs

"""
System Module

Make system calls and transactions.
"""


def test_cmd():
    pyfs.system.cmd("ls")


test_engine = TestEngine(__name__)
