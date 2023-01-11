def climbstairs(n):
    steps=[]
    steps.append(1)
    steps.append(2)
    for i in range(2,n):
        steps.append(steps[i-1]+steps[i-2])
    return steps[n-1]
n=4
print(climbstairs(n))
