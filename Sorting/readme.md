# 💰 Employee Salary Analysis Using Bubble Sort

## 📘 Project Overview

This project implements the **Bubble Sort** algorithm in Python to sort employee salaries in ascending order. After sorting, the program displays the **top 5 highest salaries** and calculates their total.

The project was developed as part of the **Data Structures Laboratory** for **Second Year B.E. Computer Engineering (Semester III)**.

---

## 🎯 Objectives

- Understand the Bubble Sort algorithm.
- Learn how adjacent element swapping works.
- Analyze the working of nested loops in sorting.
- Find the top five highest salaries after sorting.
- Calculate the sum of the top five salaries.

---

## 🛠️ Technologies Used

- **Programming Language:** Python 3
- **IDE:** Visual Studio Code / PyCharm / IDLE

---

## 📚 Data Structure Used

- **Array (Python List)**

The employee salaries are stored in a Python list and sorted using the Bubble Sort algorithm.

---

## 🔄 Algorithm Used

### Bubble Sort

Bubble Sort repeatedly compares adjacent elements and swaps them if they are in the wrong order. After each pass, the largest unsorted element moves to its correct position.


::contentReference[oaicite:0]{index=0}


### Time Complexity

| Case | Complexity |
|------|------------|
| Best Case | **O(n)** *(Already Sorted - Optimized Version)* |
| Average Case | **O(n²)** |
| Worst Case | **O(n²)** |

> **Note:** Since this program does not use the optimization (swap flag), its best-case execution also performs all comparisons, making it effectively **O(n²)**.

---

## 📋 Program Workflow

1. Enter the number of employees.
2. Enter the salary of each employee.
3. Display the unsorted list.
4. Sort the salaries using Bubble Sort.
5. Display every pass of the sorting process.
6. Print the sorted salary list.
7. Display the top five highest salaries.
8. Calculate and display the sum of the top five salaries.

---

## 💻 Sample Output

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
```

---

## 📁 Project Structure

```
📦 Employee Salary Bubble Sort
 ┣ 📜 bubblesort.py
 ┗ 📜 README.md
```

---

## ⚠️ Program Assumptions

- The number of employees should be **5 or more**, as the program displays the top five salaries.
- Salary values should be entered as integers.
- Bubble Sort is implemented manually without using Python's built-in sorting methods to better understand the Data Structures concept.

---

## 🎓 Learning Outcomes

After completing this project, students will be able to:

- Understand Bubble Sort step by step.
- Analyze nested loop execution.
- Calculate the time complexity of Bubble Sort.
- Implement sorting without using built-in functions.
- Solve simple real-world problems using sorting algorithms.

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
