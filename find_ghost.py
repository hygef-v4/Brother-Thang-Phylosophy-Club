
import os

root_dir = r"d:\Github\Brother-Thang-Phylosophy-Club"
target_file = "ch3_day3.rpy"
target_label = "label ch3_day18"

print(f"Walking {root_dir}")
for dirpath, dirnames, filenames in os.walk(root_dir):
    for f in filenames:
        if f == target_file:
            full_path = os.path.join(dirpath, f)
            print(f"FOUND FILE: {full_path}")
        
        if f.endswith(".rpy"):
            try:
                with open(os.path.join(dirpath, f), "r", encoding="utf-8") as f_obj:
                    content = f_obj.read()
                    if target_label in content:
                         print(f"FOUND LABEL IN: {os.path.join(dirpath, f)}")
            except Exception as e:
                pass
