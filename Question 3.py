

"""
Test Question 3: Power of Two
Write a program that takes an integer as input and returns true is the input is a power of two

"""

class PowerOfTwo:
    def isPowerOfTwo(self, num) -> bool:
        # Check if num is 0 and return false
        if num == 0:
            return False
        # Now loop through the digits if num is greater than 0
        while num > 0:
            # If num is 1 return true because 2 ^ 0 == 1
            if num == 1:
                return True
            # Stop iteration if num is not divisible by 2
            if num % 2 != 0:
                break
            # Continue dividing the num by 2 as long as num > 0
            num //= 2
        return False

s = PowerOfTwo()
print(s.isPowerOfTwo(144)) #returns false
print(s.isPowerOfTwo(64)) #returns true