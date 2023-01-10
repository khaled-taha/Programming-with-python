"""
8. At a certain school, student email addresses end with @student.college.edu,
   while professor email addresses end with @prof.college.edu. Write a program that first asks the
   user how many email addresses they will be entering, and then has the user enter those addresses.
   After all the email addresses are entered, the program should print out a message
   indicating either that all the addresses are student addresses or that there were some professor
   addresses entered.
"""

num_addresses = eval(input("How many email addresses will you be entering? "))
student_addresses = True
for i in range(num_addresses):
    email = input("Enter email address: ")
    if not email.endswith("@student.college.edu"):
        student_addresses = False
        break

if student_addresses:
    print("All addresses are student addresses.")
else:
    print("There were some professor addresses entered.")
