# 📝 Text Editor Using Stack (Undo & Redo Operations)

## 📘 Project Overview

This project implements a simple **Text Editor** using the **Stack** data structure in Python. It demonstrates the working of **Undo** and **Redo** operations by maintaining two stacks.

The program provides a menu-driven interface where users can:

* Add characters to the text.
* Undo the most recent operation.
* Redo the previously undone operation.
* Exit the application.

This project was developed as part of the **Data Structures Laboratory** for **Second Year B.E. Computer Engineering (Semester III)**.

---

# 🎯 Objectives

* Understand the Stack data structure.
* Learn the Last-In-First-Out (LIFO) principle.
* Implement Undo and Redo functionality using stacks.
* Practice menu-driven programming in Python.
* Apply stacks to solve real-world problems.

---

# 🛠 Technologies Used

* **Programming Language:** Python 3
* **IDE:** Visual Studio Code / PyCharm / IDLE

---

# 📚 Data Structure Used

## Stack (LIFO)

A **Stack** is a linear data structure that follows the **Last In, First Out (LIFO)** principle.

This project uses two stacks:

### 1. Undo Stack (`a`)

* Stores every character entered by the user.
* Used to perform the Undo operation.

### 2. Redo Stack (`b`)

* Stores characters removed during Undo.
* Used to restore characters during Redo.

---

# 🔄 Operations Implemented

## 1. Add Character

* Accepts a character from the user.
* Adds it to the current text.
* Pushes it onto the Undo stack.
* Clears the Redo stack.

---

## 2. Undo

* Removes the last entered character.
* Pops the character from the Undo stack.
* Pushes it onto the Redo stack.
* Updates the displayed text.

---

## 3. Redo

* Restores the most recently undone character.
* Pops the character from the Redo stack.
* Pushes it back onto the Undo stack.
* Updates the displayed text.

---

## 4. Exit

Terminates the program.

---

# 📋 Program Workflow

1. Display the menu.
2. User selects an operation.
3. Perform the selected operation.
4. Display the updated text.
5. Repeat until the user exits.

---

# 💻 Sample Output

```text
=====MENU====
1.Add
2.Undo
3.Redo
4.Exit
Enter Your Choice:1
Enter Character:H
Current Status: H
=====MENU====
1.Add
2.Undo
3.Redo
4.Exit
Enter Your Choice:1
Enter Character:e
Current Status: He
=====MENU====
1.Add
2.Undo
3.Redo
4.Exit
Enter Your Choice:1
Enter Character:l
Current Status: Hel
=====MENU====
1.Add
2.Undo
3.Redo
4.Exit
Enter Your Choice:1
Enter Character:l
Current Status: Hell
=====MENU====
1.Add
2.Undo
3.Redo
4.Exit
Enter Your Choice:1
Enter Character:k
Current Status: Hellk
=====MENU====
1.Add
2.Undo
3.Redo
4.Exit
Enter Your Choice:2
Current Status: Hell
=====MENU====
1.Add
2.Undo
3.Redo
4.Exit
Enter Your Choice:1
Enter Character:o
Current Status: Hello
=====MENU====
1.Add
2.Undo
3.Redo
4.Exit
Enter Your Choice:2
Current Status: Hell
=====MENU====
1.Add
2.Undo
3.Redo
4.Exit
Enter Your Choice:3
Current Status: Hello
=====MENU====
1.Add
2.Undo
3.Redo
4.Exit
Enter Your Choice:4
Exited

```

---

# 📁 Project Structure

```text
📦 Text-Editor-Using-Stack
│
├── TextEditor.py
└── README.md
```

---

# ⏱ Time Complexity

| Operation            | Time Complexity |
| -------------------- | --------------- |
| Add                  | O(1)            |
| Undo                 | O(1)            |
| Redo                 | O(1)            |
| Display Current Text | O(1)            |

---

# 🎓 Learning Outcomes

After completing this project, students will be able to:

* Understand the Stack (LIFO) concept.
* Implement Push and Pop operations.
* Build Undo and Redo functionality.
* Understand how stacks are used in text editors.
* Develop menu-driven applications using Python.

---

# 🌍 Real-World Applications

* Text Editors (Undo/Redo)
* Microsoft Word
* Notepad++
* VS Code
* Adobe Photoshop
* Browser Back and Forward Navigation
* IDE Code Editors

---

# ⚠️ Limitations

* Characters are added one at a time.
* The program does not check whether the Undo or Redo stack is empty before performing operations.
* Attempting to Undo or Redo when the respective stack is empty may result in an error.
* This is a console-based implementation intended for learning Data Structures.

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

* **GitHub:** https://github.com/ShlokShirole
* **LinkedIn:** https://www.linkedin.com/in/Shlok-Shirole14

---

# 📜 License

This project is created for **educational and academic purposes only** as part of the Data Structures Laboratory coursework.
