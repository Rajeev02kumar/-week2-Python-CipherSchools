mixed=(1,2,3,4.0)

# for i in mixed:
#     print(i)

# tuple withone element
nums=(1,)
words=('word1',)

print(type(nums))
print(type(words))

# tuple without paranthesis
guitars='yamaha','batom rouge','taylor'
print(type(guitars))


# tuple unpacking 
guitars=('yamaha','batom rouge','taylor')
a,b,c=(guitars)
print(a)

# list inside tuples
guitars=('yamaha','batom rouge','taylor'['tokyo ghoul theme','lanndscape'])
guitars[1].pop()
print(guitars)
guitars[1].append("we append it")
print(guitars)


