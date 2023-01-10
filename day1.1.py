
def isiso(x,y):
    if len(x)!=len(y):
        return False
    for i in range(len(x)):
        count=0
        if x.count(x[i])!=y.count(y[i]):
            return False
    return True
print(isiso("fool","poor"))
print(isiso("foal","poor"))
print(isiso("too","bar"))
print(isiso("toto","yaya"))



