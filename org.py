import sys
import os

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/scripts")

# https://stackoverflow.com/questions/436198/what-is-an-alternative-to-execfile-in-python-3
def execfile(filepath, globals=None, locals=None):
    if globals is None:
        globals = {}
    globals.update({"__file__": filepath, "__name__": "__main__"})
    with open(filepath, "rb") as file:
        exec(compile(file.read(), filepath, "exec"), globals, locals)


# https://stackoverflow.com/questions/11963019/running-python-script-from-inside-virtualenv-bin-is-not-working
activate_this = (
    os.path.dirname(os.path.realpath(__file__)) + ".\\.venv\\Scripts\\activate_this.py"
)
execfile(activate_this, dict(__file__=activate_this))

from org_internal import main

##################################
# Main
if __name__ == "__main__":
    main()
