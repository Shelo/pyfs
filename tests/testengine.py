from inspect import getmembers

import sys


class TestEngine(object):
    def __init__(self, name):
        members = getmembers(sys.modules[name])

        self.tested_total = 0
        self.ok_count = 0

        self.tests = []
        for name, f in members:
            if name.startswith("test_"):
                self.tests.append(f)

    def run_all(self):
        for test in self.tests:
            self._run(test)

    def run(self, name, expect=None):
        name = "test_" + name

        for test in self.tests:
            if test.__name__ == name:
                self._run(test, expect=expect)

    def _run(self, test, expect=None):
        if expect is None:
            try:
                test()
                self.log(True, test.__name__)
            except Exception as e:
                self.log(False, test.__name__, str(e))
        else:
            try:
                test()
                self.log(False, test.__name__,
                    "Exception " + expect.__name__ + " was expected.")
            except expect as e:
                self.log(True, test.__name__)

    def log(self, ok, test_name, error="Undefined error."):
        self.tested_total += 1

        test_name = test_name[5:]

        if ok:
            self.ok_count += 1
            print "\033[1m[Ok]\033[0m " + test_name
        else:
            print "\033[93m[Failed]\033[0m " + test_name + ": " + error

    def stats(self):
        if self.tested_total == 0:
            return "0 Tested."

        return str(self.ok_count) + " Ok out of " + str(
            self.tested_total) + " tests (" + str(
            self.ok_count * 100 / self.tested_total) + "%)\n"
