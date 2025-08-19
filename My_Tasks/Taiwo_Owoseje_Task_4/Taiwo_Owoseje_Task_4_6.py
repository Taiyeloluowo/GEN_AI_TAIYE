# Task 6: Word Analyser
analyse = input("Enter a word: ") 
upperc = analyse.isupper()
print(f"the word is in upper case: {upperc}")
lowerc = analyse.islower() 
print(f"the word is in lower case: {lowerc}") 
titlec = analyse.istitle()
print(f"the word is in lower case: {titlec}")
print(analyse[::-1])
