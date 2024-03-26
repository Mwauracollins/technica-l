
"""
Test Question 5: Reverse Integer
Write a program that takes an integer as input and returns an integer with reversed digit  ordering.
"""

class ReverseInteger:
    def reverse(self, number: int) -> int:
        if number == 0:
            return 0;
        if number < 0:
            # remove the sign fro the number
            number = abs(number)
            #convert the number to string
            str_number = str(number)
            #reverse the string
            str_number = str_number[::-1]
            #return the reversed string as an integer multiplied by -1
            return int(str_number) * -1
        elif number > 0:
            # convert number to string
            str_number = str(number)
            # reverse the string
            str_number = str_number[::-1]
            # return the reversed string as an integer
            return int(str_number)

s = ReverseInteger()
print(s.reverse(-500))