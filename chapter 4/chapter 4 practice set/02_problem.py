marks=[]

m1=float(input("Enter marks: "))
marks.append(m1)
m2=float(input("Enter marks: "))
marks.append(m2)
m3=float(input("Enter marks: "))
marks.append(m3)
m4=float(input("Enter marks: "))
marks.append(m4)
m5=float(input("Enter marks: "))
marks.append(m5)
m6=float(input("Enter marks: "))
marks.append(m6)

# short and efficient method

# for i in range(6):
#     m=float(input("Enter marks: "))
#     marks.append(m)

marks.sort()

print(marks)