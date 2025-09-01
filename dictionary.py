name={"tillu":21,
      "ramesh":42,
      "sobha":38,
      "hemanth":19}
print(name)
#print(dir(name))
#print(help(name))
print(len(name))
name.update({"roy":12})
#print(name.get("sobha"))

if name.get("tillu"):
    print("it is  belong the name")
else:
    print("it is not belongs the name")
name.pop("tillu")   
#name.clear()  
key=name.keys()
for key in name.keys( ):
 print(key)

print(name)   
