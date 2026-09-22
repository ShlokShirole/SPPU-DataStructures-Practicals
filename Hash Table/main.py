size=10
ht=[[] for _ in range(size)]
while 1:
	print("1.Insert") 
	print("2.Delete")
	print("3.Search")
	print("4.Display")
	print("5.Exit")
	ch=int(input("Enter your choice :"))
	
	if ch==1:
		v=int(input("ENTER AN ELEMENT:"))
		hk=v%size
		ht[hk].append(v)
	elif ch==2:
		v=int(input("ENTER AN ELEMENT TO DELETE:"))
		hk=v%size
		ht[hk].remove(v)
	elif ch==3:
		s=int(input("ENTER THE ELEMENT TO SEARCH"))
		hk=s%size
		flag=-1
		for item  in ht[hk]:
			if s==item:
				print("Element found at:",hk)
				flag=1
				break
		if flag==-1:
			print("Element not found")
	elif ch==4:
		for i in range (size):
			print("{0} -->  {1}".format(i,ht[i]))
		
	elif ch==5:
		break
		print("Exited..!")
