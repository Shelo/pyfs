from subprocess import call


def vim(file_path):
    call(["vim", file_path])


def confirm(text):
    while True:
        value = raw_input(text)

        if value.lower() in ('yes', 'y'):
            return True
        elif value.lower() in ('no', 'n'):
            return False
        else:
            print "Not a valid response."
