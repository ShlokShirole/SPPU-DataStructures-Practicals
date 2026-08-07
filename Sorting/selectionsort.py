n=int(input("Enter the No of Employes:"))
a=[]
for i in range(n):
	a.append(int(input("Enter the salary of employes:")))
print("Unsorted Array",a)
print("-----Selection Sort----")
for i in range(n-1):
	mi=i
	for j in range(mi+1,n):
		if a[mi]>a[j]:
			mi=j
	temp=a[mi]
	a[mi]=a[i]
	a[i]=temp
	print(i)
	print(a)
print("Sorted Array is:",a)
print("Top 5 salarys:")
sum1=0
for i in range(n-1,n-6,-1):
	print(a[i])
	sum1=sum1+a[i]
print("Sum of top 5 Salaries:",sum1)
		
