class solution:
    def maxArea(self, A):
        maxarea=0
        l=0
        r=len(A)-1
        while l<r:
            base=r-1
            height=min(A[l], A[r])
            area=base*height
            maxarea=max(area, maxarea)
            if A[l]<A[r]:
                l+=1
            else:
                r-=1
        return maxarea
ob=solution()
print(ob.maxArea([1,5,4,3]))
print(ob.maxArea([3,1,2,4,5,1]))
