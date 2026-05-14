class employee:
    a=1 # class varible 
   
    @classmethod
    def show(cls): 
      print(f"the class value of a is {cls.a}")
      
      
    @staticmethod
    def greet():
        print(f"hello user!")
             
obj1=employee()

obj1.a=40 # instance variable

obj1.greet()     
obj1.show()
