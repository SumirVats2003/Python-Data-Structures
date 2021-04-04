# stacks

# 'PUSH', 'POP', 'PEAK', 'DISPLAY'

l1 = []

def push(lst, value):
    lst.append(value)
    print("Element pushed successfully")


def pop(lst):
    p = len(lst)
    if p !=0:
        a = lst[p-1]
        del lst[p-1]
        print("Element popped successfully")
    else:
        print("There is no element in list")

def peak(lst):
    p = len(lst)
    if p != 0:
        element = lst[p-1]
        print(element)
    else:
        print("Empty List")

def display(lst):
    p = len(lst)
    if p != 0:
        for i in range(p-1,-1,-1):
            print(lst[i])
    else:
        print("Empty List")

while True:
    print("PUSH:1, POP:2, PEAK:3, DISPLAY:4, EXIT:5")
    action = int(input("Enter action:"))
    if action == 1:
        val = int(input("Enter value to push: "))
        push(l1,val)
    elif action == 2:
        pop(l1)
    elif action == 3:
        peak(l1)
    elif action == 4:
        display(l1)
    elif action == 5:
        break
    else:
        print("Please enter valid input")
