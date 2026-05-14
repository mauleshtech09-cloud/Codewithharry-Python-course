class employee:
    
    language="Python" # this is our class attribute
    salary=4000
    
abc=employee()

    
print(abc.language,abc.salary)

abc.language="JAVA" # this is our instance attribute

print(abc.language,abc.salary)
# instance attribute have more priority than class attribute while fetching data