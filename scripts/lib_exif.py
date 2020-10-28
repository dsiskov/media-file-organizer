from scripts.defaults import (
  ENV_PROCESSED_DIR_PATH_KEY,
  ENV_PROCESSING_TYPE_KEY,
  processing_type_copy
)
import os
from scripts.command_helpers import (
  run_command
)

def _get_exif_extra_parameters(file_types):
  extra_arguments = []
  for file_type in file_types:
    extra_arguments.append("-ext")
    extra_arguments.append(file_type)

  return extra_arguments

def exif_organize_by_model(args, input_path, dir_name, file_types):
  processed_dir_path = os.env.get(ENV_PROCESSED_DIR_PATH_KEY)
  output_path = os.path.join(processed_dir_path, dir_name)

  exif_command_args = [args.exif_tool_exe, exif_args_per_model.replace('PATH', output_path), "-r", input_path]
  exif_command_args.extend(_get_exif_extra_parameters(file_types))
  if os.env.getenv(ENV_PROCESSING_TYPE_KEY) == processing_type_copy:
      exif_command_args.extend(["-o", "."])

  run_command(exif_command_args, True)
  return output_path

def exif_organize_by_date(args, input_path, dir_name, file_types, file_name_with_prefix):
  processed_dir_path = os.env.get(ENV_PROCESSED_DIR_PATH_KEY)
  output_path = os.path.join(processed_dir_path, dir_name)

  exif_command_args = [args.exif_tool_exe, exif_args_per_date, "-d", f"{output_path}\\{file_name_with_prefix}", "-r", input_path]
  exif_command_args.extend(_get_exif_extra_parameters(file_types))
  if os.env.getenv(ENV_PROCESSING_TYPE_KEY) == processing_type_copy:
    exif_command_args.extend(["-o", "."])

  run_command(exif_command_args, True)