from subprocess import call


def cmd(command, *args):
    call([command] + list(args))
