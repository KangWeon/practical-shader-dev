import os
import sys
from pathlib2 import Path

def directory_search(pth, openframeworks_path): 
    if pth.is_dir(): 
        if pth.name == ".git" or pth.name == "Assets" or pth.name == "bin" or pth.name == "src": 
            return 
        for d in pth.glob("*"): 
            if d.is_dir(): 
                directory_search(d, openframeworks_path) 
            else: 
                if d.suffix == ".make" or d.name == "Makefile": 
                    text = d.read_text() 
                    text = text.replace("[put here your openframeworks path]", str(openframeworks_path)) 
                    d.write_text(text) 

def main(source_file_dir, of_path):
    root = Path(source_file_dir)
    target = Path(of_path)
    print(f"{root}")
    print(f"{target}")
    if target.exists():
        directory_search(root, target)
    else:
        print("not exist your openframeworks path!")
        exit(-1)

if len(sys.argv) != 2:
    print("usage: python your-of-path.py [your openframeworks path]")
    exit(-1)
else:
    main(os.getcwd(), sys.argv[1])

    