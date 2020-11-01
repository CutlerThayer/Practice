import string
# Create a program that translates a given string into the same string in pig latin
# If a word is capitalized maintain the capitalization on the front of the word
# If there is punctuation make sure it stays in place


# Take an input phrase
phrase = input("Please enter the phrase to translate: \n")

# Create variables
words = phrase.split()
result = ""


def lastispunctuation(x):
    if x[len(x) - 1] not in string.punctuation:
        return 0
    return 1


# Create a translator function
def translator(word):
    character = word[0]
    punctuation = ""
    if character.isupper():
        word = word[0] + word[1].upper() + word[2:]
        character = character.lower()
    puncbool = lastispunctuation(word)
    if puncbool == 1:
        punctuation = word[len(word) - 1]
        word = word[:len(word) - 1]
    word = word[1:] + character + "ay" + punctuation
    return word


# Translate each word
for x in words:
    result = result + translator(x) + " "


# Print result
print(result)
