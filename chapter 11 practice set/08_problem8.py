class Vector:
    def __init__(self,li):
        self.li=li
        
        
    def __len__(self):
        
        return len(self.li)   
        
v1=Vector([1,2,3,4,5,6])

print(len(v1)) 
       
