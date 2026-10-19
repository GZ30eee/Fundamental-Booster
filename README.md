# Fundamental Booster – Interactive Personal Data Collector

## Description
A Python console application that collects personal information, demonstrates core Python concepts (print/input, data types, variables, operators, type casting, `id()` and `type()`), and displays a formatted summary.

## Features
- Uses `input()` and `print()` for interaction.
- Demonstrates type casting (`int()`, `float()`).
- Calculates birth year using arithmetic operators.
- Displays data type and memory address of each variable.
- Shows type conversion (float → int).

## Assumptions
- Current year is obtained from the system clock.
- Height is entered in meters.
- Memory addresses vary per execution.

## How to Run
1. Ensure Python 3.x is installed.
2. Clone the repository.
3. Run: `python personal_data_collector.py`

## Sample Output
============================================================
Welcome to the Interactive Personal Data Collector!
============================================================
This program will collect some personal information from you,
perform a simple calculation, and display a summary.
Please follow the prompts.

Please enter your name: Alice
Please enter your age: 25
Please enter your height in meters: 1.68
Please enter your favourite number: 7

============================================================
Thank you! Here is the information we collected:
============================================================
Name: Alice
  Type: <class 'str'>
  Memory Address: 140703847239568

Age: 25
  Type: <class 'int'>
  Memory Address: 9793456

Height: 1.68
  Type: <class 'float'>
  Memory Address: 140703847253232

Favourite Number: 7
  Type: <class 'int'>
  Memory Address: 9793312

------------------------------------------------------------
Your birth year is approximately: 2000
  (based on your age of 25 and current year 2025)

Height in meters (float): 1.68
Height rounded down (int): 1
  (Type conversion from float to int demonstrated)

============================================================
Thank you for using the Personal Data Collector. Goodbye!
Keep exploring Python! 🐍
============================================================

## Author
GZ
