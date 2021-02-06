'''
Given an array of integers, find the pair of adjacent elements 
that has the largest product and return that product.

For example, for inputArray = [3, 6, -2, -5, 7, 3], 
the output should be adjacentElementsProduct(inputArray) = 21.

7 and 3 produce the largest product.

[input] - array
[output] - integer
'''

def adjacentElementsProduct(inputArray):
    numbers = [inputArray[i] * inputArray[i + 1] for i in range(len(inputArray) - 1)]
    return max(numbers)