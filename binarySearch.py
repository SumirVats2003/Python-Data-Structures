# binary search in list
# please input list elements in ascending order, this is a bug which needs to be fixed

def binSearch(l, key, size):
    i = 0
    j = size-1
    flag = 0
    while i<=j and flag == 0:
        mid = (i+j)//2
        if l[mid] == key:
            flag = 1
            ind = mid
        if l[mid]>key:
            j = mid - 1
        if l[mid]<key:
            i = mid+1
    
    if flag == 1:
        print('Element found at index =', ind)
    else:
        print('Element not found')


l1 = []
op = int(input("Enter number of entries: "))
for j in range(op):
    p = int(input('Enter element: '))
    l1.append(p)

num = int(input("Enter number to find: "))
binSearch(l1, num, op)
