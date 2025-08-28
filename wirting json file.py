import json
emp={"name":"tillu","age":20,"job":"students"}
filepath="os.txt"
try:
    with open(filepath,'w') as file:
        json.dump(emp,file,indent=4)
        print(f"txt file {filepath} was created")
except FileExistsError:
    print("the file is already exists")        