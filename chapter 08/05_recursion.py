def facotorial(n):
    
    if n == 0 or n == 1:
        
        return n
    
    return n*facotorial(n-1)



num=int(input("Enter number for factorial: "))
fact=facotorial(num)

print(f"Factorial of {num} = {fact}")