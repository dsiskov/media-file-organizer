import os
from os.path import isfile, join
import shutil
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

def env_value_as_list(key, as_upper=True):
  env_value = os.getenv(key)
  if as_upper:
    env_value = env_value.upper()

  return env_value.split(env_separator)

def print_colored(message, color, leave_empty_row=False):
    os.system(f"@echo on")
    print(f"{color}{message}{bcolors.ENDC}")

def is_dir_empty(dir_path):
  return len([f for f in os.listdir(dir_path) if isfile(join(dir_path, f))]) == 0

def remove_dir(dir_path):
  shutil.rmtree(dir_path)