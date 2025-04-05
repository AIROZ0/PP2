import os

path = r"C:\Users\админ\Downloads"

def path_info(path):
    if os.path.exists(path):
        return {"directory": os.path.dirname(path), "filename": os.path.basename(path)}
    return "Path does not exist"

print(path_info(path))
