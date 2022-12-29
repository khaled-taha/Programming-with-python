"""
4. (a) Write a program that asks the user to enter a sentence and then randomly rearranges the
words of the sentence. Don't worry about getting punctuation or capitalization correct.
(b) Do the above problem, but now make sure that the sentence starts with a capital, that
the original first word is not capitalized if it comes in the middle of the sentence, and
that the period is in the right place.
"""

# a)
from random import shuffle
sentence = input('Enter a sentence: ').split()
shuffle(sentence)
print(sentence)

# b)
from random import shuffle
sentence = input('Enter a sentence: ').split()
shuffle(sentence)

sentence[0] = sentence[0].capitalize()

for i in range(1, len(sentence)):
    sentence[i] = sentence[i].casefold()  

print(sentence)