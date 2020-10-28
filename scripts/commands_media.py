from scripts.defaults import (
  exif_args_per_model,
  exif_args_per_date,
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
  processed_dir_path = os.env.get(ENV_PROCESSED_DIR_PATH_KEY)
  path_exists = os.path.exists(processed_dir_path)
  if path_exists:
    #and not are_you_sure("Processed folder is not empty. Continue?", False):
    #raise Exception ('Processed path exists!')
    print('Processed path exists, will add new content there')
  
  elif not path_exists:
    # todo: bug fix making dir
    os.mkdir(processed_dir_path)

def handle_file_naming_prefix(file_naming, media_type):
  if media_type == 'IMAGE':
    return file_naming.replace(processing_file_naming_prefix, model).lower().replace('nikon', '').replace(' ', '_')

  return file_naming.replace(processing_file_naming_prefix, '')

def organize_media(args):

  print('organizing media content to ordered folders')
  _initialize_processed_folder()
  
  for media_type in env_value_as_list(ENV_PROCESSING_MEDIA_TYPES_KEY):
    input_path = os.getcwd()
    file_types = env_value_as_list(f'{media_type}_FILE_TYPES')
    file_naming_rule = handle_file_naming_prefix(os.env.get(ENV_PROCESSED_FILE_NAMING_RULE_KEY)) + exif_file_naming_duplication_rule

    if args.model:
      dir_by_model = exif_organize_by_model(input_path, f"by-model-{media_type}", file_types);
      
      if args.date:
        if not os.path.exists(input_path):
          print(f'There is no content to process in {input_path}')

        for path in Path(input_path).iterdir():
          model = str(path).split('\\')[-1]
          print(f'Processing model: {model}')
          
          file_name_with_prefix = file_naming_rule
          exif_organize_by_model(dir_by_model, f"by-date-{media_type.lower()}", file_types, file_naming_rule);

    elif args.date:
      exif_organize_by_model(input_path, f"by-date-{media_type.lower()}", file_types, file_naming_rule);





