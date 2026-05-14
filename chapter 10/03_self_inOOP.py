class employee:
    
    language="Python"
    salary=12000
    
    
    def getinfo(self):
        
        print(f"here the langauge = {self.language} and salary = {self.salary}")
        
        
maulesh=employee()
Rohit=employee()

maulesh.language="Rust"
Rohit.language="SQL"

# maulesh.getinfo() 
# both are doing the same thing , the first one is just converting in this form
employee.getinfo(maulesh)      
Rohit.getinfo()



    