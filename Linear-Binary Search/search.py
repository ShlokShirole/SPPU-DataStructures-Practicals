n=int(input("Enter no of Elements:"))
a=[]
for i in range(n):
    a.append(input("Enter Element:"))
k=input("Enter Search key:")
flag=-1
print("*******Linear Search******")
for i in range(n):
    if a[i]==k:
        print("Element found at index:",i)
        flag=i
        break
if flag==-1:
    print("Element not found")

print("******Binary Search******")
l=0
h=n-1
flag=-1
while l<=h:
    mid=int((l+h)/2)
    if a[mid]==k:
        print("Element found at index:",mid)
        flag=mid
        break
    elif k<a [mid]:
        h=mid-1
    elif k>a [mid]:
        l=mid+1

if flag==-1:
    print("Element not found ")
