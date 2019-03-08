import os

dir = os.listdir("D:")
for file in dir :                 
    if file.endswith("txt"):
        print(os.path.join("D:", file))
