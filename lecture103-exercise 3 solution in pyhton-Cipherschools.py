def reverse_element(l):
    elements=[]
    for i in l:
        elements.append(i[::-1])
    return elements
word=['abc','tuv','xyz']
print(reverse_element(word))