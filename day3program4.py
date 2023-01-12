def add_binary_nums(first, second):
    max_len = max(len(first), len(second))
    firstfill= first.zfill(max_len)
    secondfill = second.zfill(max_len)

    conversion= int(firstfill,2) + int(secondfill,2)
    result = bin(conversion)
    print(result)
add_binary_nums('1101','100')
