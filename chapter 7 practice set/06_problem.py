#5! =1x2x3x4x5

num=int(input("Enter number : "))

factorial=1

for i in range(1,num+1):
    factorial=factorial*i
    
print(f"Factorial of {num} = {factorial}")    