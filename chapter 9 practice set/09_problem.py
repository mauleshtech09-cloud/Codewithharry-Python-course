f1=open("greetings.txt","r")

content1=f1.read()

f2=open("copy_greetings.txt","r")

content2=f2.read()

if content1==content2:
    print("Yes both files content are same!")
    
    
else:
    print("No, both files content are not same!")
    
f1.close()        
f2.close()        