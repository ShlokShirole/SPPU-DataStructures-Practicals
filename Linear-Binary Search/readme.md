# 🔍 Linear Search and Binary Search in Python

## 📘 Project Overview

This project demonstrates the implementation of **Linear Search** and **Binary Search** algorithms using Python. It was developed as part of the **Data Structures Laboratory** for **Second Year B.E. Computer Engineering (Semester III)**.

The program allows the user to:
- Enter a list of elements.
- Search for a specific element using **Linear Search**.
- Search for the same element using **Binary Search**.
- Display the index of the element if found.

---

## 🎯 Objectives

- Understand the working of searching algorithms.
- Compare Linear Search and Binary Search.
- Learn the importance of sorted data in Binary Search.
- Practice Python programming for Data Structures.

---

## 🛠️ Technologies Used

- **Language:** Python 3

---

## 📂 Algorithm Used

### 1. Linear Search
Linear Search checks each element of the list one by one until the required element is found or the list ends.

**Time Complexity**
- Best Case: **O(1)**
- Average Case: **O(n)**
- Worst Case: **O(n)**

---

### 2. Binary Search
Binary Search repeatedly divides the search space into two halves to locate the target element.

> **Note:** Binary Search works only on **sorted arrays/lists**. Ensure the input list is sorted before using Binary Search.

**Time Complexity**
- Best Case: **O(1)**
- Average Case: **O(log n)**
- Worst Case: **O(log n)**

---

## 📋 Program Workflow

1. Enter the number of elements.
2. Input the list elements.
3. Enter the search key.
4. Perform Linear Search.
5. Perform Binary Search.
6. Display whether the element is found and its index.

---

## 💻 Sample Output

```
-For Element Found :
Enter no of Elements:5
Enter Element:5
Enter Element:10
Enter Element:15
Enter Element:20
Enter Element:25
Enter Search key:20
*******Linear Search******
Element found at index: 3
******Binary Search******
Element found at index: 3

-For Element Not Found :
Enter no of Elements:5
Enter Element:10
Enter Element:20
Enter Element:30
Enter Element:40
Enter Element:50
Enter Search key:60
*******Linear Search******
Element not found
******Binary Search******
Element not found


```

---

## 📁 Project Structure

```
📦 Search Algorithms
 ┣ 📜 search.py
 ┗ 📜 README.md
```

---

## ⚠️ Important Note

Binary Search requires the input list to be **sorted in ascending order**. If the list is unsorted, the Binary Search result may be incorrect.

---

## 🎓 Academic Information

- **Course:** Data Structures Laboratory
- **Program:** Bachelor of Engineering (B.E.) Computer Engineering
- **Year:** Second Year
- **Semester:** III
- **University:** Savitribai Phule Pune University (SPPU)

---

## 👨‍💻 Author

**Shlok Shirole**

- GitHub: https://github.com/ShlokShirole
- LinkedIn: https://www.linkedin.com/in/Shlok-Shirole14

---

## 📜 License

This project is created for **educational and academic purposes only** as part of the Data Structures Laboratory coursework.
