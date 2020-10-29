import os
from scripts.defaults import env_separator

def env_value_as_list(key):
  return os.getenv(key).upper().split(env_separator)