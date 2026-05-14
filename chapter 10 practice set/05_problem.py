from random import randint

class train:
    
    def __init__(self,TrainID):
        self.TrainID=TrainID
    
    def book(self,fro,to):
        print(f"Tickets booked for train with ID :- {self.TrainID} from {fro} to {to}")
        
        
    def status(self):
        print(f"train with ID :- {self.TrainID} is on the track on time! ") 
        
    def getfare(self,fro,to):
        print(f"for train with ID :- {self.TrainID} from {fro} to {to} , the total fare is {randint(222,5555)}")
        
        
rajdhani=train(101)

rajdhani.book("rajkot","goa")
rajdhani.status()
rajdhani.getfare("rajkot","kashmir")

            
        
          
        
        