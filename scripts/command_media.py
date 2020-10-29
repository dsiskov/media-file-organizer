from scripts.defaults import (
  exif_file_naming_duplication_rule,
  processing_type_copy, 
  processing_file_naming_prefix,
  ENV_PROCESSED_DIR_PATH_KEY, ENV_PROCESSING_MEDIA_TYPES_KEY, ENV_IMAGE_FILE_TYPES_KEY, ENV_VIDEO_FILE_TYPES_KEY, ENV_PROCESSED_FILE_NAMING_RULE_KEY
)
from scripts.command_helpers import (
  are_you_sure,
  run_command
)
from scripts.helpers import env_value_as_list
from scripts.lib_exif import exif_organize_by_model, exif_organize_by_date
import os
from pathlib import Path

def _initialize_processed_folder():
  processed_dir_path = os.getenv(ENV_PROCESSED_DIR_PATH_KEY)
  path_exists = os.path.exists(processed_dir_path)
  if path_exists:
    #and not are_you_sure("Processed folder is not empty. Continue?", False):
    #raise Exception ('Processed path exists!')
    print('Processed path exists, will add new content there')
  
  elif not path_exists:
    # todo: bug fix making dir
    os.mkdir(processed_dir_path)

def handle_file_naming_prefix(file_naming, media_type, model=''):
  result = file_naming.replace(processing_file_naming_prefix, model.lower())

  if media_type == 'IMAGE':
    result = result.replace('nikon', '').replace(' ', '_')

  return result

def organize_media(args):

  if not os.path.exists(args.exif_tool_exe):
    raise Exception('Exif tool not found')

  print('organizing media content to ordered folders')
  _initialize_processed_folder()

  for media_type in env_value_as_list(ENV_PROCESSING_MEDIA_TYPES_KEY):
    input_path = os.getcwd()
    file_types = env_value_as_list(f'{media_type}_FILE_TYPES')

    if args.model:
      dir_by_model = exif_organize_by_model(args, input_path, f"by-model-{media_type}", file_types);
      
      if args.date:
        if not os.path.exists(dir_by_model):
          print(f'There is no content to process in {dir_by_model}')

        for path in Path(dir_by_model).iterdir():
          model = str(path).split('\\')[-1]
          print(f'Processing model: {model}')
          
          file_naming_rule = handle_file_naming_prefix(os.getenv(ENV_PROCESSED_FILE_NAMING_RULE_KEY), media_type, model) + exif_file_naming_duplication_rule
          exif_organize_by_date(args, path, f"by-date-{media_type.lower()}", file_types, file_naming_rule);

    elif args.date:
      file_naming_rule = handle_file_naming_prefix(os.getenv(ENV_PROCESSED_FILE_NAMING_RULE_KEY), media_type, '') + exif_file_naming_duplication_rule
      exif_organize_by_date(args, input_path, f"by-date-{media_type.lower()}", file_types, file_naming_rule);





