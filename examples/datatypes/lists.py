# list is to order, get or put object in any position
list = [10, 20, 30, 40]
# tuple is imutable, like a coordinate data
tuple = (10, 20, 30, 40)
# set is like a list but you cannot order, or put/delete an element in a specific index, and each elment is unique
set1 = {10, 20, 30, 40}

print('list', list)
print('type(list)', type(list))
print('list[1]', list[1])
print('tuple', tuple)
print('type(tuple)', type(tuple))
print('tuple[1]', tuple[1])
print('set1', set1)
print('type(set1)', type(set1))
# cannot do this for set: print(set[1])

print("======== list =========")
list.append(90)
print('list after appending 90', list)
list.insert(0,100)
print('list after 100 insert(0)', list)
list.insert(0,'str')
print('list after str insert(0)', list)
list.remove('str')
print('list after removing str', list)

list.sort()
print('list after sort', list)
list.reverse()
print('list after reverse', list)
print('list.count(10)', list.count(10))
print('len(list)', len(list))


print("======== set =========")
set1.remove(20)
print('set after removing 20', set1)
set2 = {30,5,100,200}
print('set1.difference(set2)',set1.difference(set2))
print('set2.difference(set1)',set2.difference(set1))
print('set2.intersection(set1)',set2.intersection(set1))
print('set2.union(set1)',set2.union(set1))
# the set.pop method removes a random element
removed = set1.pop()
print('removed', removed)
print('set1 after removal', set1)