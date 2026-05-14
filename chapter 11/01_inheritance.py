class employee:
    company = "Balaji"
    name = "Gojo satoru"
  
    def show(self):

        print(f"the company = {self.company} and the name = {self.name}")



 # this is bad practice 
# class coder:
#     name = "Gojo satoru"
#     language = "Python"
#     salary = 12000

#     def show(self):

#         print(f"the langauge = {self.language} and the name = {self.name}")
        
#     def salary_info(self):
        
#         print(f"the name = {self.name} and salary = {self.salary}")


class coder(employee):
  
    language="Python"
    def language_info(self):
        
        print(f"the name = {self.name} and langauge he/she good at = {self.language}")
        
        
        
            
a=employee()
b=coder()  

b.show()
b.language_info()