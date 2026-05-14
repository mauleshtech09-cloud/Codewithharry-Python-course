# file = open("new.txt") this is same as this :-file= open("new.txt","r")

file = open("new.txt", "r")

data = file.read()

print(data)

file.close()
