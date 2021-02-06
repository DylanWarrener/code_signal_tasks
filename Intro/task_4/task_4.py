def adjacentElementsProduct(inputArray):
    numbers = [inputArray[i] * inputArray[i + 1] for i in range(len(inputArray) - 1)]
    return max(numbers)