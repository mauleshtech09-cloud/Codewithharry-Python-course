# def pattern(rows):
#     for i in range(rows,0,-1):
#         print("*" *i)
        
#         print()

def pattern (rows):
    if(rows==0):
        return
    
    print("*" *rows)
    pattern(rows-1)
        
        
        
rows=int(input("Enter number of rows: "))
pattern(rows)

        