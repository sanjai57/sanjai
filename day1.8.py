def isnumeric(s):
    s=s.strip()
    try:
        s=float(s)
        return True
    except:
        return False
print(isnumeric("0.2"))
print(isnumeric("xyz"))
print(isnumeric("hello"))
print(isnumeric("-2.5"))
print(isnumeric("10"))
