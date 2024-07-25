name1=input("Enter First name : ")
name2=input("Enter Second name : ")
name1 = name1.upper().replace(" ", "")
name2 = name2.upper().replace(" ", "")
common_count = 0
for char in set(name1):
    if char in name2:
        common_count += min(name1.count(char), name2.count(char))
    remaining_count = (len(name1) + len(name2)) - (2 * common_count)
    flames = list("FLAMES")
    index = 0

flames = ['Friendship', 'Love', 'Affection', 'Marriage', 'Enemies', 'Siblings']


def flameGo():
    global index
    while len(flames) > 1:

        index = (index + remaining_count - 1) % len(flames)
        flames.pop(index)
    return flames


result = flameGo()
print(f"The Flames between {name1} and {name2} is relationships of {result[0]} .")
