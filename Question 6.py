

"""
Test Question 6: Count Vowels
Write a program that counts the number of vowels in a sentence.
"""
class CountVowels:
    def countVowels(self, sentence:str) -> int:
        # initialize an array with all the posible cases of vowels
        vowels = "aeiouAEIOU"
        # initialize the counter
        count = 0
        #Loop through all the letters in the sentence
        for letter in sentence:
            #Check if letter is in the array. If so add the count by 1
            if letter in vowels:
                count += 1
        return count


s = CountVowels()
print(s.countVowels(" Hello World"))