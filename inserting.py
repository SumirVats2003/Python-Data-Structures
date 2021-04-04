# inserting elements to a list in ascending order
l1 = []

def insert(number, iList):
    for i in iList:
        if number < i:
            idx = iList.index(i)
            iList.insert(idx, number)
            break
        elif number > i:
            pass
        else:
            print("Element already in list")
    else:
        iList.append(number)
    print(iList)


ind = int(input("Enter number of entries: "))
for j in range(ind):
    p = int(input('Enter element: '))
    l1.append(p)
num = int(input("Enter number to insert: "))
insert(num, l1)
