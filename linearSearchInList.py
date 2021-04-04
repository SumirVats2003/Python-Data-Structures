# linear search in list

l1 = []

def linFind(l, f):
    for i in range(len(l)):
        if l[i] == f:
            print("Element found at index =", i)
            break
        else:
            pass
    else:
        print("Element not found")

ind = int(input("Enter number of entries: "))

for j in range(ind):
    p = int(input('Enter element: '))
    l1.append(p)

num = int(input("Enter number to find: "))
linFind(l1, num)

# 5,6,3,4,7,9,0,12,34,93
