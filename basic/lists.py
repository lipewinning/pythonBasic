friends = ['sonia', 'eduardo', 'pedro', 'dudu', 'fernanda']
print(friends[0])
print(friends[-1])
print(friends[2:])

friends[4] = 'yohan'
print(friends)

#functions
lucky_numbers = [4,8,15,16,23,42]
#friends.extend(lucky_numbers) concatenating two lists
friends.append('Rafael')
friends.insert(1, 'Paddy')
print(friends)
friends.remove('eduardo')
print(friends)
#friends.clear()
#friends.pop() remove the last element
print(friends.index('dudu'))
isInTheList = 'felipe' in friends
print(isInTheList)

friends.sort()
friends.reverse()
friends2 = friends.copy();

