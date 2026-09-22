# 🔐 Hash Table Implementation in Python

## 📘 Project Overview

This project demonstrates the implementation of a **Hash Table using Python**. It was developed as part of the **Data Structures Laboratory** for **Second Year B.E. Computer Engineering (Semester III)**.

The program uses the **Division Hashing technique** to calculate the hash index and **chaining** to store multiple elements that have the same hash value.

The program allows the user to:

* Insert an element into the hash table.
* Delete an element from the hash table.
* Search for an element.
* Display the complete hash table.
* Exit the program.

---

## 🎯 Objectives

* Understand the working of a **Hash Table**.
* Learn how **Hash Functions** are used to map elements to indexes.
* Understand **Collision Handling using Chaining**.
* Implement insertion, deletion, searching, and display operations.
* Practice Python programming for Data Structures.

---

## 🛠️ Technologies Used

* **Language:** Python 3
* **Data Structure:** Hash Table
* **Collision Handling:** Chaining
* **IDE:** Visual Studio Code

---

## 📂 Hashing Technique Used

### Division Method

The program calculates the hash index using:

```python
hk = v % size
```

Since the hash table size is:

```python
size = 10
```

the element is placed at the index obtained from the remainder.

### Example

```text
Element = 25

25 % 10 = 5
```

Therefore, `25` is stored at index `5`.

---

## 🔗 Collision Handling

The program uses **Chaining** to handle collisions.

If multiple elements generate the same hash index, they are stored in the same list.

For example:

```text
10 % 10 = 0
20 % 10 = 0
30 % 10 = 0
```

The hash table will contain:

```text
0 --> [10, 20, 30]
```

This allows multiple elements to be stored at the same hash index.

---

## ⚙️ Operations

### 1. Insert

Adds an element to the hash table.

```text
Enter your choice : 1
ENTER AN ELEMENT: 25
```

The hash index is calculated as:

```text
25 % 10 = 5
```

So the element is stored at index `5`.

---

### 2. Delete

Deletes a specified element from the hash table.

```text
Enter your choice : 2
ENTER AN ELEMENT TO DELETE: 25
```

The program calculates the hash index and removes the element from that bucket.

> The element should exist in the corresponding bucket before deletion.

---

### 3. Search

Searches for an element in the hash table.

```text
Enter your choice : 3
ENTER THE ELEMENT TO SEARCH25
Element found at: 5
```

If the element does not exist:

```text
Element not found
```

---

### 4. Display

Displays all indexes and their corresponding elements.

Example:

```text
0 -->  [10, 20, 30]
1 -->  [11]
2 -->  [12]
3 -->  []
4 -->  []
5 -->  [25]
6 -->  []
7 -->  []
8 -->  []
9 -->  []
```

---

### 5. Exit

Terminates the program.

---

## 📋 Program Workflow

1. Create a hash table of size `10`.
2. Display the menu.
3. Select an operation.
4. For insertion, calculate the hash index using `%`.
5. Store the element in the corresponding bucket.
6. For deletion, calculate the hash index and remove the element.
7. For searching, calculate the hash index and search within that bucket.
8. Display the hash table when required.
9. Exit the program.

---

## 💻 Sample Output

```text
1.Insert
2.Delete
3.Search
4.Display
5.Exit

Enter your choice :1
ENTER AN ELEMENT:10

Enter your choice :1
ENTER AN ELEMENT:20

Enter your choice :1
ENTER AN ELEMENT:11

Enter your choice :4

0 -->  [10, 20]
1 -->  [11]
2 -->  []
3 -->  []
4 -->  []
5 -->  []
6 -->  []
7 -->  []
8 -->  []
9 -->  []
```

### Search Example

```text
Enter your choice :3
ENTER THE ELEMENT TO SEARCH20
Element found at: 0
```

### Element Not Found

```text
Enter your choice :3
ENTER THE ELEMENT TO SEARCH50
Element not found
```

---

## 📁 Project Structure

```text
📦 Hash Table
 ┣ 📜 main.py
 ┗ 📜 README.md
```

---

## ⚠️ Important Note

The hash table size used in this program is:

```python
size = 10
```

The hash index is calculated using:

```python
element % size
```

The program uses **chaining** to handle collisions by storing multiple elements in the same list.

---

## 🎓 Academic Information

* **Course:** Data Structures Laboratory
* **Program:** Bachelor of Engineering (B.E.) Computer Engineering
* **Year:** Second Year
* **Semester:** III
* **University:** Savitribai Phule Pune University (SPPU)

---

## 👨‍💻 Author

**Shlok Shirole**

* GitHub: https://github.com/ShlokShirole
* LinkedIn: https://www.linkedin.com/in/Shlok-Shirole14

---

## 📜 License

This project is created for **educational and academic purposes only** as part of the Data Structures Laboratory coursework.
