n=int(input("Enter the No of Employes:"))
a=[]
for i in range(n):
	a.append(int(input("Enter the salary of employes:")))
print("--------Bubble Sort-------")
print("Unsorted Array:")
for i in range(n-1):
	for j in range(n-i-1):
		if a[j]>a[j+1]:
			temp=a[j]
			a[j]=a[j+1]
			a[j+1]=temp
		print(a)
	print("Outer",a)
print("Sorted Array:",a)
print("Top 5 Salarys:")
sum1=0
for i in range(n-1,n-6,-1):
	print(a[i])
	sum1=sum1+a[i]
print("Sum of top 5 Salary:",sum1)
