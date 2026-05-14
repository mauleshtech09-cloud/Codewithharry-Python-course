with open("twinkle_twinkle.txt","r") as file:
    
    content=file.read()
    
    word=input("Enter a word to search : ")
    
    if (word in content):
        print(f"{word} found in the file!")
        
    else:
        print(f" {word} Not found in the file!")    