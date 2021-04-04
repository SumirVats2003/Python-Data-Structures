l1 = []

def delete(dList, number, size):
    flag = 0
    i = 0
    j = size - 1
    if number in dList:
        while i<=j and flag == 0:
            mid = (i+j)//2
            if dList[mid] == number:
                flag = 1
                pos = mid
            if dList[mid] > number:
                j = mid - 1
            if dList[mid] < number:
                i = mid+1
        del dList[pos]
        print(dList)
    else:
        print("Element not in List")
    return dList

ind = int(input("Enter number of entries: "))
for j in range(ind):
    p = int(input('Enter element: '))
    l1.append(p)
num = int(input("Enter number to delete: "))

delete(l1, num, ind)

