# def greater(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>c and b>a:
#         return b
#     else:
#         return c

# a=int(input("enter a first number : "))
# b=int(input("enter a second number : "))
# c=int(input("enter a third number : "))
# bigger = greater(a,b,c)
# print(f"{bigger} is a greater number")

def new_greater(a,b,c):
    bigger=new_greater(a,b)
    return new_greater(bigger,c)
print(new_greater(1000,200,30))