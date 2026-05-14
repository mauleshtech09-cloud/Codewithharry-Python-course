def maxnum(num1,num2,num3):
    if(num1>num2 and num1>num3):
        return (f"{num1} is greatest")
    
    elif(num2>num1 and num2>num3):
        return (f"{num2} is greatest")
    
    if(num3>num1 and num3>num2):
        return (f"{num3} is greatest")
    
    if(num1==num2 and num2==num3):
        return (f"All are equel!,{num1}=={num2}=={num3}")
    
    else:
        return (f"Something went wrong!")
    
    
num1=int(input("Enter a number: "))   
num2=int(input("Enter a number: "))   
num3=int(input("Enter a number: "))
    
print(maxnum(num1,num2,num3))    