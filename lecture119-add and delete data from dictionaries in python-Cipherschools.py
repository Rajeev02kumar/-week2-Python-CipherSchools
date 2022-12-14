user_info={
    'name':'harshit',
    'age':'24',
    'fav_movie':['coco','kiwi no na wa'],
    'fav_tunes':['awaking','fairy tale']
}

user_info['fav_songs']=['user1','song2']
print(user_info)

#pop method
popped_item=user_info.pop('fav_tunes')
print(f"popped item is {popped_item}")
print(user_info)


#popitem method
popped_item=user_info.popitem()
print(user_info)
print(type(popped_item))