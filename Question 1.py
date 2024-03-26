"""
Test Question 1: FizzBuzz
Write a program that prints the numbers from 1 to 100. For multiples of 3, print "Fizz"; for
multiples of 5, print "Buzz"; and for numbers that are multiples of both 3 and 5, print
"FizzBuzz".

"""


class FizzBuzz:
    def fizzBuzz(self):
        for i in range(1, 101):
            # Start with checking if the conditions are met in both
            if i % 3 == 0 and i % 5 == 0:
                print(f"{i} is FizzBuzz")
            # Now check the conditions individually
            elif i % 3 == 0:
                print(f"{i} is Fizz")
            elif i % 5 == 0:
                print(f"{i} is Buzz")


s = FizzBuzz()
s.fizzBuzz()