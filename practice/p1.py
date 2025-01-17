class xx():
    a=55
    def __init__(self,n):
        print("class never changes its instance",n)
b=xx("badshah")
print(b.a)
b.a=0
print(b.a)