class employee:

    name = "Maulesh"
    age = 18
    salary = 3000000

    def getinfo(self):

        print(f"here the langauge = {self.name} and salary = {self.salary}")
        
    @staticmethod
    def greet():
        
        print("Hello , user!")   


maulesh = employee()

maulesh.greet()
maulesh.getinfo() 