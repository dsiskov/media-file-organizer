from scripts.defaults import (
  ENV_PROCESSED_DIR_PATH_KEY,
  ENV_PROCESSING_TYPE_KEY,
  processing_type_copy,
  exif_args_per_date,
  exif_args_per_model
)
import os
from scripts.command_helpers import (
  run_command
)

def _get_exif_initial_args(exe_path):
  exif_command_args = [exe_path]
  if os.getenv(ENV_PROCESSING_TYPE_KEY).upper() == processing_type_copy:
    exif_command_args = exif_command_args + ["-o", "."]

  return exif_command_args

def _run_exif_command(args):
  run_command(args, True)

def _get_exif_extra_parameters(file_types):
  extra_arguments = []
  for file_type in file_types:
    extra_arguments.append("-ext")
    extra_arguments.append(file_type)

  return extra_arguments

def exif_organize_by_model(args, input_path, dir_name, file_types):
  processed_dir_path = os.getenv(ENV_PROCESSED_DIR_PATH_KEY).replace('\\', '\\\\')
  output_path = os.path.join(processed_dir_path, dir_name)

  exif_command_args = _get_exif_initial_args(args.exif_tool_exe) + [exif_args_per_model.replace('PATH', output_path), "-r", input_path]
  exif_command_args.extend(_get_exif_extra_parameters(file_types))

  _run_exif_command(exif_command_args)
  return output_path

def exif_organize_by_date(args, input_path, dir_name, file_types, file_name_with_prefix):
  processed_dir_path = os.getenv(ENV_PROCESSED_DIR_PATH_KEY)
  output_path = os.path.join(processed_dir_path, dir_name)

  exif_command_args = _get_exif_initial_args(args.exif_tool_exe) + [exif_args_per_date, "-d", f"{output_path}\\{file_name_with_prefix}", "-r", input_path]
  exif_command_args.extend(_get_exif_extra_parameters(file_types))
  
  _run_exif_command(exif_command_args)
  