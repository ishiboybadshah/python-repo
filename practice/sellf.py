class addition:
    def __init__(self,n):
        self.n=list(n)
    def __sub__(self,other):
        for i in other.n:
            if i in self.n:
             self.n.remove(i)
        return (self.n)
    
ob1=addition("abidtys")
ob2=addition("anjht")

print(ob1-ob2)

            