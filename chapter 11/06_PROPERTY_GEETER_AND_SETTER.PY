class employee:
    a=1 # class varible 
   
    @classmethod
    def show(cls): 
      print(f"the class value of a is {cls.a}")
      
    @property
    def name(self):
          
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self,value):
        self.fname = value.split(" ") [0]
        self.lname = value.split(" ") [1]
            
             
obj1=employee()     

obj1.a=40 # instance variable

obj1.name="Jiya Modi"
print(obj1.fname, obj1.lname)

