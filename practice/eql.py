class addition:
    def __init__(self,n):
        self.n=str(n)
    def __eq__(self,other):
        if self.n==other.n:
            return True
        return False
       
    
ob1=addition("ad")
ob2=addition("adowpf")

print(ob1==ob2)