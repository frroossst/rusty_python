import json
import os
import re

def read_settings():

    with open("settings.json","r") as fobj:
        content = json.load(fobj)

    return content

def git_ignore(param):

    pass

def setup():

    template = {
        "default_file_name" : "main.rs",
        "after_lint" : "run",
        "gitignore" : False,
        "create_new" : True
        }

    lint = {
        "println!" : "print"
        }

    if os.path.exists("settings.json"):
        pass
    else:
        with open("settings.json","w") as fobj:
            json.dump(template,fobj)
            fobj.close()

    #git_ignore()

def read_source(file):

    with open(file,"r") as fobj:
        source = fobj.read()

    return source


def after_lint(cmd):

    if cmd == "run":
        os.system("cargo run")

    elif cmd == "build":
        os.system("cargo build")


def linter():

    setup()

    settings = read_settings()

    source = read_source(settings["file"])

    print(settings)

    lints = {}

    with open("lints.json","r") as fobj:
        lints = json.load(fobj)

    # Replacement lints
    for i,j in lints.items():
        print(i,"=>",j)
        pattern = i
        replacement = j


    after_lint(settings["after_lint"])
