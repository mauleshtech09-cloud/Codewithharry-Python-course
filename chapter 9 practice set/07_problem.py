f = open("log.txt","r")

lines=f.readlines()

lineno =1
for line in lines:

    if "python" in line:
        print(f"yes python is in the content!, at line : {lineno}")
        break
    lineno+=1
        
else:
    print(f"No, python is not in the content!")
        
f.close()     