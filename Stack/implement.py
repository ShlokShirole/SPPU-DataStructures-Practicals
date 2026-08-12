
text=""
a=[]
b=[]

while 1:
	print("=====MENU====")
	print("1.Add")
	print("2.Undo")
	print("3.Redo")
	print("4.Exit")
	m=int(input("Enter Your Choice:"))
	if m==1:
		ch=input("Enter Character:")
		text=text+ch
		a.append(ch)
		b.clear()
		print("Current Status",text)

	elif m==2:
		x=a.pop()
		text=text[:-1]
		b.append(x)
		print("Current Status",text)

	elif m==3:
		x=b.pop()
		a.append(x)
		text=text+x
		print("Current Status",text)

	elif m==4:
		print("Exited")
		break
