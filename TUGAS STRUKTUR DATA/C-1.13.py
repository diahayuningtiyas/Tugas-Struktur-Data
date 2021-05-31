def myReverse(data):
    # returning a new reversed list
    return [data[i] for i in range(len(data)-1, -1, -1)]
print(myReverse([2, 4, 6, 8, 10, 12, 14]))
