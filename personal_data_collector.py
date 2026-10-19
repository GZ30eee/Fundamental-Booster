"""
Fundamental Booster - Interactive Personal Data Collector
Author: [Your Name]
Date: [Current Date]
Description: Collects personal information, demonstrates data types, variables,
             operators, type casting, and built-in functions id() and type().
"""

import datetime

def main():
    # ---------- Welcome and Instructions ----------
    print("=" * 60)
    print("Welcome to the Interactive Personal Data Collector!")
    print("=" * 60)
    print("This program will collect some personal information from you,")
    print("perform a simple calculation, and display a summary.")
    print("Please follow the prompts.\n")

    # ---------- Collect Information ----------
	    name = input("Please enter your name: ")
	    age_str = input("Please enter your age: ")
	    height_str = input("Please enter your height in meters: ")
	    fav_num_str = input("Please enter your favourite number: ")

    # ---------- Type Casting ----------
    age = int(age_str)               # Convert age to integer
    height = float(height_str)       # Convert height to float
    fav_num = int(fav_num_str)       # Convert favourite number to integer

    # ---------- Data Processing ----------
    current_year = datetime.date.today().year
    birth_year = current_year - age

    # Convert height to integer (rounded down) for demonstration
    rounded_height = int(height)

    # ---------- Display Results with type() and id() ----------
    print("\n" + "=" * 60)
    print("Thank you! Here is the information we collected:")
    print("=" * 60)

    print(f"Name: {name}")
    print(f"  Type: {type(name)}")
    print(f"  Memory Address: {id(name)}")

    print(f"\nAge: {age}")
    print(f"  Type: {type(age)}")
    print(f"  Memory Address: {id(age)}")

    print(f"\nHeight: {height}")
    print(f"  Type: {type(height)}")
    print(f"  Memory Address: {id(height)}")

    print(f"\nFavourite Number: {fav_num}")
    print(f"  Type: {type(fav_num)}")
    print(f"  Memory Address: {id(fav_num)}")

    # ---------- Calculations and Type Conversion Explanation ----------
    print("\n" + "-" * 60)
    print(f"Your birth year is approximately: {birth_year}")
    print(f"  (based on your age of {age} and current year {current_year})")

    print(f"\nHeight in meters (float): {height}")
    print(f"Height rounded down (int): {rounded_height}")
    print(f"  (Type conversion from float to int demonstrated)")

    # ---------- Exit Message ----------
    print("\n" + "=" * 60)
    print("Thank you for using the Personal Data Collector. Goodbye!")
    print("Keep exploring Python! 🐍")
    print("=" * 60)

if __name__ == "__main__":
    main()
