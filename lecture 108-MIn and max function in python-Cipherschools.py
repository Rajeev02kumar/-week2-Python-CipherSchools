numbers=[6,60,2]

# print(min(numbers))
# print(max(numbers))

def greater_diff(l):
    return max(l)-min(l)

print(greater_diff(numbers))