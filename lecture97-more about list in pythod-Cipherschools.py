# generator list with range function 

# number = list(range(1,11))
# # print(number)

# number.pop()
# print(number )

# popped_item = number.pop ()
# print(number.index(5))


# number =[1,2,3,4,5,6,7,8,9,10,1,5,4,8,1,6,8]
# print(number.index(1,3,14))

number=[1,2,3,4,5,6,7,8,9,10]
def negative_list(l):
    negative=[]
    for i in l:
        negative.append(-i)
    return negative
print(negative_list(number))



