
path = r"C:\Users\админ\Desktop\PROGA2\PP2\LAB_6\dir-and-files\t3.py"

def write_list_to_file(file_path, lst):
    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(f"{item}\n" for item in lst)

write_list_to_file(path, ["apple", "banana", "cherry"])
