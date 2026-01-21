import shutil
import os

if os.path.exists("app.log"):
    for i in range(1, 6):
        shutil.copy("app.log", f"app_{i}.log")
    print("Log files duplicated successfully.")
else:
    print("app.log not found!")
