f=open("old.txt","r")

content=f.read()

f2=open("renamed_by_python.txt","w")

f2.write(content)