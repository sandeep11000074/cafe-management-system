# Royal Cafe Management System

A simple **Python-based Cafe Management System** that allows users to view cafe information, check the menu, place orders, and generate a final bill.

This project is designed to demonstrate the use of basic Python concepts such as **variables, dictionaries, lists, tuples, functions, loops, conditional statements, exception handling, and user input**.

## Features

*  Display cafe information
*  Display available food items and prices
*  Place customer orders
*  Enter quantity for each item
*  Validate invalid item names and quantities
*  Generate a final bill
*  Calculate the total bill automatically
*  Exit the program safely

##  Concepts Used

The project demonstrates:

* **Dictionary** – Stores menu items and their prices
* **List** – Stores customer orders
* **Tuple** – Stores cafe information
* **Functions** – Divides the program into different tasks
* **For Loop** – Displays menu and calculates the bill
* **While Loop** – Handles continuous ordering and main menu
* **If-elif-else** – Handles user choices
* **Try-except** – Handles invalid quantity input
* **f-strings** – Formats the displayed output
* **Input/Output** – Takes user input and displays results

##  Menu

| Item     | Price |
| -------- | ----: |
| Coffee   |   ₹80 |
| Tea      |   ₹40 |
| Burger   |  ₹120 |
| Pizza    |  ₹200 |
| Sandwich |  ₹100 |

##  Project Structure

```text
Royal-Cafe-Management-System/
│
├── royal_cafe.py
└── README.md
```

##  How to Run

### 1. Install Python

Make sure Python is installed on your computer.

Check your Python version:

```bash
python --version
```

### 2. Clone the Repository

```bash
git clone <your-github-repository-url>
```

### 3. Open the Project Folder

```bash
cd Royal-Cafe-Management-System
```

### 4. Run the Program

```bash
python royal_cafe.py
```

##  How the Program Works

After starting the program, the user gets the following options:

```text
1. Cafe Information
2. Show Menu
3. Place Order
4. Generate Bill
5. Exit
```

### Cafe Information

Displays:

* Cafe name
* Location
* Opening and closing time

### Show Menu

Displays all available food items along with their prices.

### Place Order

The user can enter an item name and quantity.

Example:

```text
Enter item name or type 'done' to finish: Pizza
Enter quantity: 2

2 x Pizza added to your order.
```

### Generate Bill

The program calculates the price of each ordered item and displays the total amount.

Example:

```text
==============================
           BILL
==============================
Pizza x 2 = Rs. 400
Tea x 1 = Rs. 40
------------------------------
Total Bill = Rs. 440
==============================
```

## Purpose of the Project

The main purpose of this project is to practice and demonstrate fundamental Python programming concepts by building a small real-world application.

It can be useful for beginners who are learning:

* Python data types
* Functions
* Loops
* Conditional statements
* Exception handling
* Basic program structure

##  Future Improvements

The project can be extended by adding:

* Customer name and contact details
* GST/tax calculation
* Discount system
* Multiple customers
* Order cancellation
* Receipt generation
* File/database storage
* Graphical User Interface (GUI)
* Login system
* Online ordering functionality

##  Author

**Sandeep Parashar**

B.Tech CSE (AI & ML)
VIT Bhopal University

##  License

This project is created for **educational and learning purposes**.
