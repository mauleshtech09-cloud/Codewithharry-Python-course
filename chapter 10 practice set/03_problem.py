class demo:
    a=4
    
    
o=demo()

print(o.a) # prints the class attribute because instance attribute is not present 

o.a=0 # set the instance attribute

print(o.a) # prints the instance attribute because instance attribute is present 

print(demo.a) # this prints the class attribute    