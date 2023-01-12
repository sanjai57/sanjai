def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
s =  "12345"
print("the original string is : ", end="")
print(s)
print("the reversed string(using loops) is : ", end="")
print(reverse(s))
