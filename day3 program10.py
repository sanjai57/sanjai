def editDistanceHelper(i, j, str1, str2):
    if i==0:
        return j
    if j==0:
        return i
    ans = 1+ min(
        {
            editDistanceHelper(i, j - 1, str1, str2), # insert
            editDistanceHelper(i - 1, j, str1, str2), # remove
            editDistanceHelper(i - 1, j - 1, str1, str2), # replace
        }
    )
    if str1[i - 1]==str2[j - 1]:
        ans=min(ans, editDistanceHelper(i - 1, j - 1, str1, str2))


    return ans


def editDistance(str1, str2):
    n=len(str1)
    m=len(str2)
    ans=editDistanceHelper(n, m, str1, str2)
    return ans
print(editDistance("insertion", "execution"))
    
