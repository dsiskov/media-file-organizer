import os
import sys
import argparse
from scripts.command_media import organize_media
from dotenv import load_dotenv
load_dotenv()

def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ("yes", "true", "t", "y", "1"):
        return True
    elif v.lower() in ("no", "false", "f", "n", "0"):
        return False
    else:
        raise argparse.ArgumentTypeError("Boolean value expected.")

def create_parser():

    parser = argparse.ArgumentParser(
        description="Tool to bulk organize media files"
    )

    exif_commands = ["media"]
    all_commands = exif_commands

    parser.add_argument("command", help="the command", choices=all_commands)

    parser.add_argument(
        "-d",
        "--date",
        type=str2bool,
        nargs="?",
        const=True,
        default=False,
        help=f"Using .env settings, copy/move media to output folder by date.\r\nCan be combined with --model",
    )

    parser.add_argument(
        "-m",
        "--model",
        type=str2bool,
        nargs="?",
        const=True,
        default=False,
        help=f"Using .env settings, copy/move media to output folder by model.\r\nCan be combined with --date",
    )

    parser.add_argument(
        "-p",
        "--prefix",
        default="",
        help=f"Prefix of processed file names. Default value is empty. Use MODEL to replace with extracted model value",
    )

    parser.add_argument(
        "-t",
        "--tag",
        default="CreateDate",
        choices=["FileModifyDate", "CreateDate"],
        help=f"Tag used for processing file names. Default value is CreateDate",
    )

    parser.add_argument(
        "--output_dir_img",
        default="",
        help=f"If not specified, used from .env",
    )

    parser.add_argument(
        "--output_dir_vid",
        default="",
        help=f"If not specified, used from .env",
    )

    parser.add_argument(
        "--input_dir",
        default=None,
        help=f"Full path to input directory. Current working directory used when not defined",
    )

    return parser

def execute_command(command, args):
  if command == "media":
    organize_media(args)

def main():
  os.system(f"@echo on")
  parser = create_parser()
  args = parser.parse_args()

  args.exif_tool_exe = os.path.dirname(os.path.realpath(__file__)) + "/tools/exiftool.exe"

  try:
    execute_command(args.command, args)
  except:
    error = f"{sys.exc_info()[1]}"
    print(error)
    sys.exit(1)

if __name__ == "__main__":
    main()