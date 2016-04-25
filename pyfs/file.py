import shutil
import os


def copy(fp_from, fp_to):
    shutil.copyfile(fp_from, fp_to)


def remove(fp, ignore=False):
    try:
        os.remove(fp)
    except OSError as e:
        if not ignore:
            raise e
