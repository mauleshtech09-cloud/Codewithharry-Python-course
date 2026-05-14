class employee:
    language="Python"
    salary=12000
    
    def __init__(self,name,language,salary): # this is dunder method which is automatically called
        
        self.name=name
        self.language=language
        self.salary=salary        
        print("I am dunder method!")
    
    
    def getinfo(self):
        
        print(f"here the langauge = {self.language} and salary = {self.salary}")
        
        
maulesh=employee("Maulesh","Kali linux",5000000,)

print(maulesh.name,maulesh.language,maulesh.salary)

maulesh.getinfo()


