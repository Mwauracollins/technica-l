

"""
Test Question 4: Capitalize Words
Write a program that accepts a string as input, capitalized the first letter of each word in the
string and then returns the result string
"""

class Capitalize:
    def capitalize(self, phrase:str) -> str:

        #Separate the words in the sentence

        words = phrase.split()
        new_str = ""
        print(words)
        for word in words:
            # select the first letter of the word and make it uppercase then add the rest of the word
            capitalized_word = word[0].upper() + word[1:]
            # Add the word to the new string with a space
            new_str += capitalized_word + " "
        return new_str.strip()





s = Capitalize()
print(s.capitalize("i love programming"))
