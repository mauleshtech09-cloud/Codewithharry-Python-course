f=open("greetings.txt","r")

content=f.read()


f2=open("copy_greetings.txt","w")

f2.write(content)

f.close()

f2.close()