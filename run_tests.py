from tests import *

if __name__ == '__main__':
    # file_tests.test_engine.run("copy")
    # file_tests.test_engine.run("remove")
    # file_tests.test_engine.run("remove", expect=OSError)
    # file_tests.test_engine.run("remove_force")
    # print file_tests.test_engine.stats()

    text_tests.test_engine.run("replace")

    # prompt_tests.test_engine.run("vim")
    # prompt_tests.test_engine.run("confirm")
    # print prompt_tests.test_engine.stats()
