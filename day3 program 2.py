first_num=int(input("enter the first number..."))
second_num=int(input("enter the second number..."))
third_num=int(input("enter the third number..."))
my_list=[]
print("the first number is ")
print(first_num)
print("the second number is ")
print(second_num)
print("the third number is ")
print(third_num)
my_list.append(first_num)
my_list.append(second_num)
my_list.append(third_num)
for i in range(0, 3):
    for j in range(0, 3):
        for k in range(0, 3):
            if(i!=j&j!=k&k!=i):
                print(my_list[i],my_list[j], my_list[k])
