# I have commented out nearly all of the code so that it would be easy to use it in fragments, because all of the fragments are indepenent


a = []

''' QUESTION 1 '''
# for i in range(5):
#     a.append(i)
# a = [i for i in range(5)]

''' QUESTION 2 '''
# for i in range(1, 50):
#     if i % 7 == 0:
#         a.append(i)
# a = [i for i in range(1,50) if i%7==0]

''' QUESTION 3 '''
# a = [num if num<5 else num*2 for num in range(2,9)]
# for i in range(2,9):
#     if i < 5:
#         a.append(i)
#     else:
#         a.append(i*2)

''' QUESTION 4 '''
# vals = [31,15,42,12,5,39,21,61,25]
# a = [i for i in vals if i%3==0]

''' QUESTION 5 '''
# lst = [('a', 11), ('b', 12), ('c', 13)]
# a = [n*3 for (x,n) in lst if x=='b' or x=='c']
# output predicted: [36,39]
# output received: [36,39]

''' QUESTION 5 '''
# for x in [10, 5, 2]:
#     for y in [2,3,4]:
#         a.append(x**y)
# output predicted: [100, 1000, 10000, 25, 125, 625, 4, 8, 16]
# output received: [100, 1000, 10000, 25, 125, 625, 4, 8, 16]
# a = [x**y for x in [10,5,2] for y in [2,3,4]]


print(a)
