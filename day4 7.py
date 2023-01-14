def countstrings(n, start):
    if n==0:
        return 1
    count=0
    for i in range(start, 5):
        count += countstrings(n - 1, i)
    return count
def countVowelStrings(n):
    # char arr[5]={'a','e','i','o','u'};
    # starting from index 0 add the vowels to strings
    return countstrings(n, 0)
n = 1
print(countVowelStrings(n))
