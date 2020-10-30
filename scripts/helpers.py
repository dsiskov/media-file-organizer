import os
from scripts.defaults import (
  env_separator, env_keyvalue_separator,
  ENV_PREFIX_REPLACE_VALUES_KEY
)

class bcolors:
    WARNING = '\033[93m'
    HEADER = '\033[95m'
    LINK = '\033[94m'
    INFO = '\033[90m'
    ENDC = '\033[0m'
    STATUS = '\033[96m'

def env_value_as_list(key):
  return os.getenv(key).upper().split(env_separator)

def print_colored(message, color, leave_empty_row=False):
    os.system(f"@echo on")
    print(f"{color}{message}{bcolors.ENDC}")