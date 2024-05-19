from collections import Counter
list = [1, 1, 2, 2, 3, 3, 4, 4]
kle = []
for num in list:
    print(num)
    kle.append(num)
    print(kle)
counter=Counter(list)
print(kle)
duplicates = [item for item, count in counter.items() if count > 1]
if duplicates:
    print('\n \n')
    print(duplicates)
    print(len(duplicates))
