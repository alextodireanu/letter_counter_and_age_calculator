# For a given string it adds the character to a dictionary and counts how many times the character appears in the string
def letter_counter(text):
    """Method to count the characters in a given string"""
    characters = {}
    for character in text:
        characters[character] = text.count(character)
    return characters


phrase = input("Insert the word or phrase here -> ")
print(letter_counter(phrase))
