import os
from scripts.defaults import env_separator

def env_value_as_list(key):
  return os.env.get(key).upper().split(env_separator)