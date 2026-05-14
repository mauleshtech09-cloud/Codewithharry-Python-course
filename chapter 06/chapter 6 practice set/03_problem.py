p1="iphone for free"
p2="click here"
p3="free money"
p4="free prize"

comment=input("Enter your comment : ")

if (p1 in comment) or (p2 in comment) or (p3 in comment) or (p4 in comment):
    print(f"{comment} comment is a spam!")
    
    
else:
    print(f"{comment} comment is not a spam!")    