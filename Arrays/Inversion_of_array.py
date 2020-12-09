def mergeSort(arr,left,right):
    inv_count = 0
    if left < right:
        mid = (left+right)//2
        inv_count += mergeSort(arr,left,mid)
        inv_count += mergeSort(arr,mid+1,right)
        inv_count += merge(arr,left,mid,right)
    return inv_count
    
def merge(a,left,mid,right):
    i = left
    j = mid+1
    k = left
    count = 0
    temp = []
    
    while i < mid+1 and j < right+1:
        if a[i]<=a[j]:
            temp.append(a[i])
            i += 1
        else:
            temp.append(a[j])
            j += 1
            count += (mid-i+1)
        
    while i <= mid:
        temp.append(a[i])
        i += 1
        
    while j < right+1:
        temp.append(a[j])
        j += 1
        
    
    
    for loop in range(left,right+1):
        arr[loop] = temp[loop-left]
    return count
    
for _ in range(int(input())):
    n = int(input())
    arr = input().split()
    for i in range(n):
        arr[i] = int(arr[i])
    print(mergeSort(arr,0,n-1))
        