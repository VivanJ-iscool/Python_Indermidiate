#Homework
#1
def sum_all(*nums):
    ans = 0
    for num in nums:
        ans += num
    return ans

print(sum_all(3,4,77,223))

#2
def word_lenght(collection):
    c = 1
    for item in collection:
        c += 1
    return item and c

print(word_lenght("bruuuuuuuh"))

#3
def rangee(end, start=0, steps=1):
    lst = []
    counter = start
    if start < end:
        while counter < end:
            lst.append(counter)
            counter += steps
        return lst
    elif start > end:
        while counter >= end:
            lst.append(counter)

print(rangee(11))

#4 & 5
lst2 = [2, 6, 8, 7]
def slicer(lst, start = 0, end = -1, step = 1):
        slice = []
        if end == -1:
            end = len(lst) - 1
        for element in range(start, end, step):
            slice.append(lst[element])
        return slice

print(slicer(lst2))

a=90
def gv():
    global a
    a+= 10
    print(a)

gv()
#6
#One local variable is the variable slice which is a string. Question 4
#Second local variable can be c in question 2, which takes the value of 1
#The final local variable can be ans in question 1, which takes the value of 0
