user_info={
    'name':'harshit',
    'age':'24',
    'fav_movie':['coco','kiwi no na wa'],
    'fav_tunes':['awaking','fairy tale']
}

if 'name' in user_info:
    print('present')
else:
    print('not present')


if 'haarshit' in user_info.values():
    print('present')
else:
    print('not present')

# for i in user_info.value():
#     print(i)

user_info_values=user_info.values()
print(user_info_values)
print(type(user_info_values))

for i in user_info:
    print(user_info[i])


# item method

user_item=user_info.value()
print(type(user_item))

# for key,value in user_info_items():
    # print(f"key is {key} and value is {value}")






