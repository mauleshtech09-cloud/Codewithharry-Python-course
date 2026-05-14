post=input("Enter your post : ")

information=input("Enter information you want to find: ")

if(information.lower() in post.lower()):
    print(f"yes this post is talking about {information}!")
    
    
else:
    print(f"No, this post is not talking about {information}")   