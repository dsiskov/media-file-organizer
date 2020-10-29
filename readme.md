# Command line media files organizer tool

## Install

Make sure python is installed, in sys path variables and can execute .py files  
Execute

```cmd
pip3 install pipenv
```

Run `firstrun.bat` in Administrator CMD

## **media** command (Win)

**requirements**:  
Download exif_tool from https://exiftool.org/, place in root folder `./tools`

**args**:  
`--date`: process media structured by date  
`--model`: process media structured by model

**tips**:
When both used together, files are placed in folders by date, filenames include model name as prefix
```python
org media -d -m
```
