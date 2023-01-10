"""
3. People often forget closing parentheses when entering formulas. Write a program that asks
the user to enter a formula and prints out whether the formula has
the same number of opening and closing parentheses.
"""
formula = input("Enter a formula: ")
open_count = formula.count("(")
close_count = formula.count(")")
if open_count == close_count:
    print("The formula has the same number of opening and closing parentheses.")
else:
    print("The formula does not have the same number of opening and closing parentheses.")


