f = open("log.txt","r")

content=f.read()

if "python" in content:
    print(f"yes python is in the content! ")
    
else:
    print(f"No, python is not in the content!")
    
f.close()        