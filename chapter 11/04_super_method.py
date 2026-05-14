class vehicle:
    
    def __init__(self):
        print("Constructor of vehicle")
        
    name=input("Enter name of vehicle: ")
    company=input("Enter company name : ")

    def show(self):
        
        print(f"name of vehicle = {self.name} and company name = {self.company}")
        
class flying_vehicles(vehicle):
    
    def __init__(self):
        print("Constructor of flying_vehicle")
    
    def show_flying_info(self):
        
        print(f"name of vehicle = {self.name} and company name = {self.company}")
        
class aeroplane(flying_vehicles):
    
    def __init__(self):
        super().__init__()
        print("Constructor of aeroplane")
    
    model=input("Enter model name : ")
    
    def aeroplane_details(self):
        
        print(f"Name of vehicle = {self.name} , company name = {self.company} , and model = {self.model}")        
    

# obj=vehicle()
obj2=flying_vehicles()
obj3=aeroplane()

# obj.show()
# obj2.show_flying_info()
# obj3.aeroplane_details()
    