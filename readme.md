# Command line media files organizer tool

## Prerequisite

Installed Python 3.9, set up in sys path variables
Installed pipenv
```cmd
pip3 install pipenv
```
To set-up virtual environment for tool, run `firstrun.bat` in Administrator CMD

## **media** command (Win)

**requirements**:  
Download exif_tool from https://exiftool.org/, place in root folder `./tools`

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
