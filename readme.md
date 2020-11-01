# Command line media files organizer tool

## Prerequisite

- Have Python 3.9 installed, set up in sys path variables
- Have installed pipenv

```cmd
pip3 install pipenv
```

- Set-up virtual environment for tool, run `firstrun.bat` in Administrator CMD
- Create `.env` file (see `.env.example`)
- See help:

```py
organize --help
```

## **media** command (Win)

Organizing media content based on user settings defined in `.env` file
Files that don't match organizing criteria are not affected

**requirements**:  
Download exif_tool from https://exiftool.org/, place in folder `./tools` (same level as `organize.py`)

**args**:  
`--date`: process media structured by date  
`--model`: process media structured by model
`--prefix`: filename prefix

**usage**:

```python
..\<media-folder-to-organize>\organize media -d
```

**tips**:

1.  When both used together, files are placed in folders by date
    If desired, filenames can include model name as prefix with running

```python
..\<media-folder-to-organize>\organize media -d -m -p MODEL_
```

2.  To fully reorganize existing photo/video structure into new one

- set `PROCESSING_TYPE=move`
- define all camera models with replacement strings, `PREFIX_REPLACE_VALUES`
- run `organize media -d -p unk_`
- navigate to PROCESSED_IMAGE_DIR_PATH/PROCESSED_VIDEO_DIR_PATH
- run `organize media -m -d -p MODEL_`

**NOTE**  
Files that are not affected by Exiftool (create date/model missing) will not be moved to output folder
