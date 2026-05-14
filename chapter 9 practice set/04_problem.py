word="Donkey"

with open("new.txt","r") as f:
    content=f.read()
    
contentnew=content.replace(word,"####")

with open("new.txt","w") as f:
    f.write(contentnew)