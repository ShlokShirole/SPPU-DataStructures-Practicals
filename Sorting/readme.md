# 💰 Employee Salary Analysis Using Bubble Sort and Selection Sort

## 📘 Project Overview

This project demonstrates the implementation of two fundamental sorting algorithms:

* **Bubble Sort**
* **Selection Sort**

The program accepts employee salary details, sorts them in ascending order using the selected sorting algorithm, displays the sorted salary list, and calculates the **Top 5 Highest Salaries** along with their total.

This project was developed as part of the **Data Structures Laboratory** for **Second Year B.E. Computer Engineering (Semester III)**.

---

# 🎯 Objectives

* Understand the working of Bubble Sort and Selection Sort.
* Learn the concept of sorting using arrays (Python Lists).
* Compare the behavior of different sorting algorithms.
* Find the Top 5 highest employee salaries.
* Calculate the sum of the Top 5 salaries.

---

# 🛠 Technologies Used

* **Programming Language:** Python 3
* **IDE:** Visual Studio Code / IDLE / PyCharm

---

# 📚 Data Structure Used

* **Array (Python List)**

Employee salaries are stored in a Python list and sorted using manual implementations of sorting algorithms without using Python's built-in `sort()` function.

---

# 🔄 Algorithms Implemented

## 1. Bubble Sort

Bubble Sort repeatedly compares adjacent elements and swaps them if they are in the wrong order. After every pass, the largest unsorted element moves to its correct position.

### Time Complexity

| Case         | Complexity |
| ------------ | ---------- |
| Best Case    | O(n²)*     |
| Average Case | O(n²)      |
| Worst Case   | O(n²)      |

> *Since this implementation does not use the swap optimization, the best-case complexity also remains O(n²).*

### Advantages

* Simple to understand.
* Easy to implement.
* Suitable for small datasets.

### Disadvantages

* Inefficient for large datasets.
* Performs many unnecessary comparisons.

---

## 2. Selection Sort

Selection Sort repeatedly finds the minimum element from the unsorted portion of the array and places it at its correct position.

### Time Complexity

| Case         | Complexity |
| ------------ | ---------- |
| Best Case    | O(n²)      |
| Average Case | O(n²)      |
| Worst Case   | O(n²)      |

### Advantages

* Requires fewer swaps than Bubble Sort.
* Easy to understand.
* Performs well for small datasets.

### Disadvantages

* Not suitable for large datasets.
* Time complexity remains O(n²) in every case.

---

# 📋 Program Workflow

1. Enter the number of employees.
2. Enter each employee's salary.
3. Display the unsorted salary list.
4. Sort the salaries using:

   * Bubble Sort
   * Selection Sort
5. Display the sorted salary list.
6. Print the Top 5 highest salaries.
7. Calculate and display the total of the Top 5 salaries.

---

# 💻 Sample Output

## Bubble Sort

```
Enter the No of Employees: 6

Enter the salary of employees:
45000
30000
60000
50000
70000
55000

--------Bubble Sort-------
Unsorted Array:
[45000, 30000, 60000, 50000, 70000, 55000]

Sorted Array:
[30000, 45000, 50000, 55000, 60000, 70000]

Top 5 Salaries:
70000
60000
55000
50000
45000

Sum of Top 5 Salary:
280000

---

## Selection Sort

Enter the No of Employes:7
Enter the salary of employes:45000
Enter the salary of employes:85000
Enter the salary of employes:75000
Enter the salary of employes:95400
Enter the salary of employes:20000
Enter the salary of employes:10000
Enter the salary of employes:78000
Unsorted Array [45000, 85000, 75000, 95400, 20000, 10000, 78000]
-----Selection Sort----
0
[10000, 85000, 75000, 95400, 20000, 45000, 78000]
1
[10000, 20000, 75000, 95400, 85000, 45000, 78000]
2
[10000, 20000, 45000, 95400, 85000, 75000, 78000]
3
[10000, 20000, 45000, 75000, 85000, 95400, 78000]
4
[10000, 20000, 45000, 75000, 78000, 95400, 85000]
5
[10000, 20000, 45000, 75000, 78000, 85000, 95400]
Sorted Array is: [10000, 20000, 45000, 75000, 78000, 85000, 95400]
Top 5 salarys:
95400
85000
78000
75000
45000
Sum of top 5 Salaries: 378400

---

# 📁 Project Structure

```
📦 Employee-Salary-Sorting
│
├── BubbleSort.py
├── SelectionSort.py
└── README.md
```

---

# 🎓 Learning Outcomes

After completing this project, students will be able to:

* Understand Bubble Sort algorithm.
* Understand Selection Sort algorithm.
* Compare Bubble Sort and Selection Sort.
* Analyze the time complexity of sorting algorithms.
* Apply sorting techniques to solve real-world problems.
* Find the highest salaries using sorted data.

---

# 📊 Algorithm Comparison

| Feature       | Bubble Sort       | Selection Sort            |
| ------------- | ----------------- | ------------------------- |
| Technique     | Adjacent Swapping | Minimum Element Selection |
| Swaps         | More              | Fewer                     |
| Best Case     | O(n²)*            | O(n²)                     |
| Average Case  | O(n²)             | O(n²)                     |
| Worst Case    | O(n²)             | O(n²)                     |
| Easy to Learn | Yes               | Yes                       |

---

# ⚠️ Assumptions

* The number of employees should be **5 or more**.
* Salary values should be entered as integers.
* Sorting is performed manually without using Python's built-in sorting methods to understand DSA concepts.

---

# 🎓 Academic Information

* **Course:** Data Structures Laboratory
* **Program:** Bachelor of Engineering (B.E.) Computer Engineering
* **Year:** Second Year
* **Semester:** III
* **University:** Savitribai Phule Pune University (SPPU)

---

# 👨‍💻 Author

**Shlok Shirole**

* GitHub: https://github.com/ShlokShirole
* LinkedIn: https://www.linkedin.com/in/Shlok-Shirole14

---

# 📜 License

This repository is created **for educational and academic purposes only** as part of the Data Structures Laboratory coursework. Anyone is free to use it for learning and reference.
