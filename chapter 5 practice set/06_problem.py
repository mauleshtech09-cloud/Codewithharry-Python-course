d={}

name=input("Enter name of friend 1 : ")
lang=input("Enter language of friend 1 : ")

d.update({name:lang})

name=input("Enter name of friend 2 : ")
lang=input("Enter language of friend 2 : ")

d.update({name:lang})

name=input("Enter name of friend 3 : ")
lang=input("Enter language of friend 3 : ")

d.update({name:lang})

name=input("Enter name of friend 4 : ")
lang=input("Enter language of friend 4 : ")

d.update({name:lang})

# print(d.items())

# better and efficient way:-

# for i in range(1,5):
#     name=input(f"Enter name of friend {i}: ")
#     lang=input(f"Enter language of friend {i}: ")
    
#     d.update({name:lang})
    
print(d)