path = r"C:\Users\админ\Desktop\PROGA2\PP2\LAB_6\dir-and-files\t3.py"

def count_lines(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return sum(1 for _ in f)

print(count_lines(path))
