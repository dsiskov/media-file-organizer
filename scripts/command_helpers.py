from subprocess import run
import sys

def run_command(args, capture_output=False, hide_command_args=False, encoding="utf-8"):
    try:
        result = run(args, capture_output=capture_output, universal_newlines=True, encoding=encoding)
    except:
        error = f"{sys.exc_info()[1]}"
        raise Exception(f"Exception while executing external command {args[0]}.\n{error}")

    return result

def are_you_sure(question, quit=True):
    areyousure = input(f"{question} ").lower()
    if not areyousure == 'y':
        if quit:
            print('user-abort. \nexit tool')
            exit(0)
        else:
            print('skipped')
            return False
    return True