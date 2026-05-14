marks=int(input("Enter marks , between 0 to 100: "))

if(marks>90 and marks<=100):
    print(f"EX (extraordinary passed) with {marks} marks")
    
elif(marks>80 and marks<=90):
    print(f"A (A grade  passed) with {marks} marks")
    
elif(marks>70 and marks<=80):
    print(f"B (B grade  passed) with {marks} marks")
    
elif(marks>60 and marks<=70):
    print(f"C (C grade  passed) with {marks} marks")
    
elif(marks>=50 and marks<=60):
    print(f"D (D grade  passed) with {marks} marks")
    
elif(marks<50):
    print(f"F (F grade Fail) with {marks} marks")
    
    
        
    
    