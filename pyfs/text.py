from subprocess import call


def replace(file_path, args):
    with open(file_path, "r+") as f:
        text = f.read()

        for find, replacement in args:
            text = text.replace(find, replacement)

        f.seek(0)
        f.write(text)
        f.truncate()


def contains(file_path, what):
    return None
