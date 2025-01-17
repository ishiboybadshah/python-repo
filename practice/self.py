class addition:
    def __init__(self,n):
        self.n=n
    def __add__(self,other):
        for i in other.n:
            self.n.add(i)
        return self.n
    
ob1=addition({3,4,6})
ob2=addition({8,9,4})   

print(ob1+ob2)
    