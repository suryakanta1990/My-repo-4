List = [100, 2, 300, 10, 11, 1000]

largest_number = List[0]

for a in List:
    if a > largest_number:
        largest_number = a

print(largest_number)