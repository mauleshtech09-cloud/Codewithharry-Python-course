def sum(num):
    if(num==1):
        return 1
    return sum(num-1) + num



num=int(input("Enter a number: "))
total_sum=sum(num)

print(f"sum = {total_sum}")