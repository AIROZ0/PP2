def copy_file(src, dest):
    with open(src, "r", encoding="utf-8") as f1, open(dest, "w", encoding="utf-8") as f2:
        f2.write(f1.read())

path = r"C:\Users\админ\Desktop\PROGA2\PP2\LAB_6\dir-and-files\t3.py"
path2 = r"C:\Users\админ\Desktop\PROGA2\PP2\LAB_6\dir-and-files\t3_copy.py"

copy_file(path, path2)
