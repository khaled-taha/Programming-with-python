"""
3. (a) Ask the user to enter a sentence and print out the third word of the sentence.
(b) Ask the user to enter a sentence and print out every third word of the sentence.
"""

# a)
sentence = input('Enter a sentence: ').split()
try:
    print(sentence[2])
except:
    print("Out of bound")

# b)
sentence = input('Enter a sentence: ').split()
words = [sentence[i] for i in range(0, len(sentence), 3)]

