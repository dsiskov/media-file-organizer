# Win command line file organizer tool

## Install

Make sure python is installed, in sys path variables and can execute .py files  
Execute

```cmd
pip3 install pipenv
```

Run `firstrun.bat` in Administrator CMD

## **media** command

**requirements**:  
exif_tool from https://exiftool.org/, place in `./tools`

**args**:  
`--date`: process media structured by date  
`--model`: process media structured by model

**usage**:

```python
org media -d -m
```
