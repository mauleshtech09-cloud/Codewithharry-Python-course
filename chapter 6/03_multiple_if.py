age=int(input("Enter your age: "))

if(age%2==0):
    print("age is even!")

if (age>=18):
    print(f"Your age {age} is above the requiered age, you can go for movie!")
    
elif(age<0):
    print(f"You are entering negetive age : {age}, which is invalid!")
    
elif(age==0):
    print(f"You are entering age : {age}, which is invalid!")        
    
else:
   print(f"Your age {age} is below the requiered age, you cannot go for movie!")
   
if(age%2!=0):
    print("age is odd!")   
  
print("Program ended successfully!")  