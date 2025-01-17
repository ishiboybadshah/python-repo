import random

class train():
    def __init__(self,trainNo):
        self.trainNo=trainNo
        
    def book(self,frm,to):
        print(f"train ticket {self.trainNo} is booked {frm}-{to}")
        
    def getInfo(self):
        print(f"train ticket {self.trainNo} is on time")
            
    def getFare(self,frm,to):
        print(f"ticket fare in {self.trainNo} from {frm}-{to} is {random.randint(234,567)}")
        
        
        
t=train(16755)
t.book("gulbarga","bengaluru")
t.getFare("gulbarga","bengaluru")
t.getInfo()