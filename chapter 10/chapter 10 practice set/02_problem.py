class calculator:
    
    def __init__(self,n):
        
        self.n=n
        
        
    def square(self):
        print(f"Square is {self.n * self.n}")
            
    def cube(self):
        print(f"Cube is {self.n * self.n * self.n}") 
           
    def squareroot(self):
        print(f"Squareroot is {self.n ** 1/2}") 
        
        
obj1=calculator(5)

obj1.square()           
obj1.cube()        
obj1.squareroot()          