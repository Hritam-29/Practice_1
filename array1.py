#Linear Search and Binary Search

def LinearSearch(arr,value):
    for i in range(len(arr)):
        if(arr[i]==value):
            return i
    return -1

lst=[1,2,3,4,5,6,7]
to_find=5
ans=LinearSearch(lst,to_find)
print(ans)



def BinarySearch(arr,val):
   low=0
   high=(len(arr)-1)

   while (low<=high):
      mid=(low+high)//2
      if(arr[mid]==val):
         return mid
      if(arr[mid]<val):
         low=mid+1
      else:
         high=mid-1
   return -1

print (BinarySearch(lst,to_find))


