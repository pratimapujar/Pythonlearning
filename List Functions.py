lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Keren", "Jim", "Oscar", "Toby"]
friends.extend(lucky_numbers)
print(friends)

friends = ["Kevin", "Keren", "Jim", "Oscar", "Toby"]
friends.insert(1, "Kelly")
print(friends)

friends = ["Kevin", "Keren", "Jim", "Oscar", "Toby"]
friends.remove("Jim")
print(friends)

friends = ["Kevin", "Keren", "Jim", "Oscar", "Toby"]
friends.clear()
print(friends)

friends = ["Kevin", "Keren", "Jim", "Oscar", "Toby"]
friends.pop()
print(friends)

friends = ["Kevin", "Keren", "Jim", "Oscar", "Toby"]
print(friends.index("Oscar"))

friends = ["Kevin", "Keren", "Jim", "Jim", "Oscar", "Toby"]
print(friends.count("Jim"))

friends = ["Kevin", "Keren", "Jim", "Jim", "Oscar", "Toby"]
friends.sort()
print(friends)

lucky_numbers = [46, 33, 8, 15, 16, 23, 42]
lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers = [46, 33, 8, 15, 16, 23, 42]
lucky_numbers.reverse()
print(lucky_numbers)

friends = ["Kevin", "Keren", "Jim", "Oscar", "Toby"]
friends2 = friends.copy()
print(friends2)