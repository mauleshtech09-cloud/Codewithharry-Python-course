class employee:
    company="Google"
    name="Unknown"
    
    def info(self):
        
            print(f"name = {self.name} and company = {self.company}")
            
            
class technical:
    company="google"
    designation="Software developer"
    
    def show_designation(self):
        
        print(f"desigantion = {self.designation}")
        
        
class cybersecurity(employee,technical):
    
    name="Maulesh"
    designation="threat analyst"
    
    def info_cyber(self):
        print(f"name = {self.name} designation = {self.designation} company = {self.company}")
        
        
cyber=cybersecurity()

cyber.info_cyber()                            