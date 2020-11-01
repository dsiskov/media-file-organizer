from scripts.defaults import (
  exif_file_naming_duplication_rule,
  processing_type_copy, 
  processing_file_model_prefix,
  ENV_PROCESSED_IMAGE_DIR_PATH_KEY, ENV_PROCESSED_VIDEO_DIR_PATH_KEY, ENV_PROCESSING_MEDIA_TYPES_KEY, ENV_IMAGE_FILE_TYPES_KEY, ENV_VIDEO_FILE_TYPES_KEY, ENV_PROCESSED_FILE_NAMING_RULE_KEY, ENV_PREFIX_REPLACE_VALUES_KEY, ENV_PREFIX_SUFFIX_KEY,
  all_env_keys, env_keyvalue_separator,
  keyword_image, keyword_video
)
from scripts.command_helpers import (
  run_command
)
from scripts.helpers import env_value_as_list, bcolors, print_colored, is_dir_empty, remove_dir
from scripts.lib_exif import exif_organize_by_model, exif_organize_by_date
import os
from pathlib import Path

def _initialize_output_dir(output_dirs):
  for key, processed_dir_path in output_dirs.items():
    path_exists = os.path.exists(processed_dir_path)
    if path_exists:
      media_type = key.lower()
      print_colored(f'Processing {media_type}s to an existing loacation, adding new content', bcolors.INFO, True)
    
    elif not path_exists:
      try:
        # todo: bug fix making dir
        os.mkdir(processed_dir_path)
      except:
        raise Exception(f'Please manually create directory {processed_dir_path}')

def handle_file_naming_prefix(file_naming, media_type, file_prefix, model=''):
  model_to_lower = model.lower()
  index_to_insert = file_naming.rfind('\\') + 1
  naming_with_prefix = file_naming[:index_to_insert] + file_prefix + file_naming[index_to_insert:] 
  result = naming_with_prefix.replace(processing_file_model_prefix, f'{model_to_lower}')

  for prefix_replacement in env_value_as_list(ENV_PREFIX_REPLACE_VALUES_KEY, False):
    split = prefix_replacement.split(env_keyvalue_separator)
    if not len(split) == 2:
      raise Exception(f'User setting (.env) key: {ENV_PREFIX_REPLACE_VALUES_KEY} is not defined properly')
    
    key = split[0].lower()
    replacement = split[1]
    result = result.replace(key, replacement)

  return result

def _validate(args):
  if not os.path.exists(args.exif_tool_exe):
    raise Exception('Exif tool not found')

  for env_key in all_env_keys:
    if not os.getenv(env_key):
      raise Exception(f'User setting (.env) key: {env_key} is not defined!')

def organize_media(args):

  print_colored('Start organizing media content...', bcolors.STATUS, True)
  
  _validate(args)

  output_dir = { 
    keyword_image: os.getenv(ENV_PROCESSED_IMAGE_DIR_PATH_KEY),
    keyword_video: os.getenv(ENV_PROCESSED_VIDEO_DIR_PATH_KEY),  
  }
  _initialize_output_dir(output_dir)

  for media_type in env_value_as_list(ENV_PROCESSING_MEDIA_TYPES_KEY):
    print_colored(f'Processing {media_type}s...', bcolors.INFO, True)

    input_path = os.getcwd()
    file_types = env_value_as_list(f'{media_type}_FILE_TYPES')

    if args.model:

      if args.date:
        temp_output_dir = os.path.join(output_dir[media_type], '_temp')
        if not os.path.exists(temp_output_dir):
          os.mkdir(temp_output_dir)

        dir_by_model = exif_organize_by_model(args, input_path, temp_output_dir, file_types);
      
        if not os.path.exists(dir_by_model):
          print_colored(f'There is no content to process in {dir_by_model}', bcolors.INFO, True)

        for path in Path(dir_by_model).iterdir():
          model = str(path).split('\\')[-1]
          print_colored(f'Processing model: {model}', bcolors.INFO, True)
          
          file_naming_rule = handle_file_naming_prefix(os.getenv(ENV_PROCESSED_FILE_NAMING_RULE_KEY), media_type, args.prefix, model) + exif_file_naming_duplication_rule
          exif_organize_by_date(args, path, output_dir[media_type], file_types, file_naming_rule);

        if is_dir_empty(temp_output_dir):
          remove_dir(temp_output_dir)
        else:
          print_colored(f'There are unprocessed files placed in {temp_output_dir}', bcolors.INFO, True)

      else:
        dir_by_model = exif_organize_by_model(args, input_path, output_dir[media_type], file_types);


    elif args.date:
      file_naming_rule = handle_file_naming_prefix(os.getenv(ENV_PROCESSED_FILE_NAMING_RULE_KEY), media_type, args.prefix, '') + exif_file_naming_duplication_rule
      exif_organize_by_date(args, input_path, output_dir[media_type], file_types, file_naming_rule);

  print_colored('Finished successfully!', bcolors.STATUS, True)



