# 📋 Event Processing Using Queue in Python

## 📘 Project Overview

This project demonstrates the implementation of an **Event Processing System using Queue** in Python. It was developed as part of the **Data Structures Laboratory** for **Second Year B.E. Computer Engineering (Semester III)**.

The program uses the **Queue data structure** to manage and process events. It provides options to insert, process, display, and cancel events.

The program allows the user to:

* Enter the capacity of the queue.
* Insert new events into the queue.
* Process events from the queue.
* Display the current queue.
* Cancel a specific event.
* Exit the program.

---

## 🎯 Objectives

* Understand the working of the **Queue data structure**.
* Learn the **FIFO (First In, First Out)** principle.
* Implement queue operations using Python.
* Understand event processing using a queue.
* Practice Python programming for Data Structures.

---

## 🛠️ Technologies Used

* **Language:** Python 3
* **Data Structure:** Queue
* **IDE:** Visual Studio Code

---

## 📂 Data Structure Used

### Queue

A **Queue** is a linear data structure that follows the:

> **FIFO (First In, First Out)** principle.

This means that the element inserted first will be processed first.

Example:

```text
Front                         Rear
  ↓                            ↓
[10] → [20] → [30] → [40]
```

If the queue processes an event, `10` will be processed first.

---

## ⚙️ Queue Operations

### 1. Insert

Adds a new event to the queue.

```text
Queue:
10 → 20 → 30

Insert 40

10 → 20 → 30 → 40
```

---

### 2. Process

Processes the next event in the queue.

```text
Before:

10 → 20 → 30

Process

10 is processed first.
```

---

### 3. Display

Displays the elements currently present in the queue.

Example:

```text
Queue:
[10, 20, 30]
```

---

### 4. Cancel

Allows the user to cancel a specific event from the queue.

Example:

```text
Queue:
[10, 20, 30, 40]

Cancel: 30

Queue:
[10, 20, 40]
```

---

### 5. Exit

Terminates the program.

---

## 📋 Program Workflow

1. Enter the capacity of the queue.
2. Display the menu.
3. Select an operation.
4. Insert an event if required.
5. Process an event when required.
6. Display the queue.
7. Cancel a specific event if required.
8. Exit the program.

---

## 💻 Sample Output

### For Insert and Display

```text
Enter the capacity: 5

1. Insert
2. Process
3. Display
4. Cancel
5. Exit

Enter your Choice: 1
Enter The Elements: 101

1. Insert
2. Process
3. Display
4. Cancel
5. Exit

Enter your Choice: 1
Enter The Elements: 102

1. Insert
2. Process
3. Display
4. Cancel
5. Exit

Enter your Choice: 3
[101, 102]
```

### For Processing an Event

```text
Enter your Choice: 2
```

The first event in the queue is processed.

### For Cancelling an Event

```text
Enter your Choice: 4
Process to cancel. 102
```

The specified event is removed from the queue.

### For Queue Full

```text
Enter your Choice: 1
Queue Is Full
```

---

## 📁 Project Structure

```text
📦 Event Processing using Queue
 ┣ 📜 main.py
 ┗ 📜 README.md
```

---

## ⚠️ Important Notes

* The queue has a fixed capacity entered by the user.
* Events are processed according to the **FIFO** principle.
* An event must exist in the queue to be cancelled.
* The program displays **Queue Is Full** when the queue reaches its capacity.
* The program displays **Queue is Empty** when there are no events available for processing.

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
