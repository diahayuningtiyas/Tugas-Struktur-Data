from typing import List


def isProductOdd(data: List[int]) -> (int, int):
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if (data[i] != data[j]) and ((data[i] * data[j]) % 2 == 1):
                return data[i], data[j]
    return False


def isProductOddOptimized(data: List[int]) -> (int, int):
    oddElements = {x for x in data if x % 2 == 1}
    if len(oddElements) > 1:
        return oddElements.pop(), oddElements.pop()
    return False


data = [3, 7, 7, 9]

print(isProductOdd(data))
print(isProductOddOptimized(data))
