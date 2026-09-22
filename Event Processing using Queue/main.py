mx = int(input("Enter the capacity: "))

f = r = -1

q = []

while 1:

    print("1. Insert")
    print("2. Process")
    print("3. Display")
    print("4. Cancel")
    print("5. Exit")

    ch = int(input("Enter your Choice: "))

    if ch == 1:

        if r >= mx - 1:
            print("Queue Is Full")

        else:
            r = r + 1
            q.append(int(input("Enter The Elements: ")))

    elif ch == 2:

        if f == r or r == -1:
            print("Queue is Empty")

        else:
            f = f + 1
            q[f] = None

    elif ch == 3:

        print(q)

    elif ch == 4:

        k = int(input("Process to cancel."))

        ind = -1

        for i in range(len(q)):

            if q[i] == k:
                ind = i
                break

        if ind == -1:
            print("Element Not Exist.")

        else:

            for i in range(ind, len(q) - 1):
                q[i] = q[i + 1]

            q[len(q) - 1] = None

    elif ch == 5:

        break

    else:

        print("Invalid Choice")