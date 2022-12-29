"""
5. Write a simple quote-of-the-day program. The program should contain a list of quotes, and
when the user runs the program, a randomly selected quote should be printed.
"""

from random import choice
quotes = [
    "Make each day your masterpiece. --John Wooden",
    "Your imagination is your preview of life's coming attractions. --Albert Einstein",
    "Someday is not a day of the week. --Denise Brennan-Nelson",
    "It's time to start living the life you've imagined --Henry James"
]

print(choice(quotes))