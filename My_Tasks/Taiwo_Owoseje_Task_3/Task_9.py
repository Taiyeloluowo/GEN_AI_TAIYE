# Task 2_9
# Ask the user to enter a sentence and print the number of vowels in it.
phrase = input("What do you think about this programme? ")
num_vowels = phrase.count("a") + phrase.count("e") + phrase.count("o") + phrase.count("i") + phrase.count("a")
print(num_vowels)