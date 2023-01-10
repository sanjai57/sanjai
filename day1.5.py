fresh=int(input("enter the number of fresh loves purchased"))
old=int(input("enter the number of day old loaves purchased"))
print("regular price:rs.185.00")
fresh_amount=185.00*float(fresh)
old_amount=(185*0.4)*float(old)
total=fresh_amount+old_amount
print("amount of new loaves:Rs" ,fresh_amount)
print("amount of day old loaves:Rs" ,old_amount)
print("total amount:Rs",total)
