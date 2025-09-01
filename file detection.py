import os
filepath="os.txt"  #foldername/filename.extensation
if os.path.exists(filepath):  #using the path valuues
    print(f" the file '{filepath}' is exists in desk")
    if os.path.isfile(filepath):
        print(" it is a file")
    elif os.path.isdir(filepath):
        print(" it is a directory")
else:
    print("some thing went wrong")