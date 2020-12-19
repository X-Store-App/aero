import os


def default():
    print("Installing modules")
    os.system("pipenv install")

def build():
    print("Building Aero")
    os.system("pyinstaller main.py --onefile -n aero")
