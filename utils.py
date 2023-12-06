import pathlib
import os
from unidecode import unidecode

def extensionChanger(path, newExtension):

    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            if os.path.splitext(file)[1] == newExtension:
                print(f"{file} is already {newExtension}")
                continue
            else:
                pathlib.Path(os.path.join(path, file)).rename(os.path.join(path, file).replace(os.path.splitext(file)[1], newExtension))
                print(f"{file} was renamed to {file.replace(os.path.splitext(file)[1], newExtension)}")


def getFile(path):
    files = []
    try:
        for file in os.listdir(path):
            if os.path.isfile(os.path.join(path, file)):
                files.append(file.replace(".txt", ""))
        print(f"Đang xử lý các files: {files}")
    except Exception as e:
        print(e)
    return files


def remove_accents(text):
    return unidecode(text).replace(" ", "").lower().replace("\n", "")

def nl_remove_accents(text):
    return unidecode(text).replace(" ", "").replace("\n", "")