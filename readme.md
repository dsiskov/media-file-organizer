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

**usage**:

```python
..\<media-folder-to-organize>\organize media -d
```

**tips**:
When both used together, files are placed in folders by date, filenames include model name as prefix

```python
..\<media-folder-to-organize>\organize media -d -m
```
