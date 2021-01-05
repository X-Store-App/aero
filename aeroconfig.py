import os
import subprocess
from pathlib import Path
from datetime import datetime, timezone
import json

def default():
    print("Installing modules")
    os.system("pipenv install")

def build():
    print("Building Aero")
    print("Creating metadata")
    # get date
    date = datetime.now(timezone.utc)
    # get last commit
    commit = subprocess.check_output(["git", "describe"]) # , "--tags"])
    # now we output all this information to a json friendly file in our dist folder
    file = Path('./dist/build.json')
    jsonData = json.dumps(obj={
        "date": date.isoformat(),
        "commit": str(commit)
    })
    file.write_text(jsonData)
    # and create the app itself
    os.system("pyinstaller main.py --onefile -n aero")
