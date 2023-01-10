def onedigit(num):
    return((num>=0) and
           (num<10))
def isbhavana(num, dupNum):
    if onedigit(num):
        return(num == (dupNum[0])%10)
    if not isbhavana(num // 10, dupNum):
        return False
    dupNum[0]=dupNum[0]//10
    return(num%10==(dupNum[0])%10)
def isbhav(num):
    # if num is negative,
    # make it positive
    if(num<0):
        num=(-num)
    dupNum=[num] #*dupNum=num
    return isbhavana(num, dupNum)
n=12321
if isbhav(n):
    print("yes")
else:
    print("no")

                     
