

"""
Test Question 2: Fibonacci Sequence
Write a program to generate the Fibonacci sequence up to 100.

//NOTE: A fibonacci is a sequence of numbers where the next number in the
sequence is the sum of the previous two numbers in the sequence.
0, 1, 1, 2, 3, 5, 8, 13, ..., and
"""

class Fibonacci:
    def fibonacci(self):
        # Lets start by defining the aviables "a" and "b" and initializing them as the 0, 1
        a, b = 0, 1
        # Initialize an empty array
        arr = []

        """
        Now we loop through 100 while reinitializing the value of a
        to be the second value and the new b will be the sum of a and b
        """
        while a < 100:
            # add a to the array
            arr.append(a)

            a, b = b, a + b

        print(arr)

s = Fibonacci()
s.fibonacci()