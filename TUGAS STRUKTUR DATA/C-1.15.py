from typing import List


def areDistinct(data: List[int]) -> bool:
    uniqueNums = {x for x in data}
    return len(uniqueNums) == len(data)


data1 = [2, 4, 6, 8, 3, 1]
data2 = [2, 5, 6, 2, 5, 4]
print(areDistinct(data1))
print(areDistinct(data2))
