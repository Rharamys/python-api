dict1 = { "Banana": 10, "Apple": 20, "Peach": 30 }
dict2 = { 10: "Banana", 20: "Apple", 30: "Peach" }
print('dict1', dict1)
print('type(dict1)', type(dict1))
print('dict2', dict2)
print('type(dict2)', type(dict2))

print('dict1["Apple"]',dict1["Apple"])
print('dict2[30]',dict2[30])

dict1['Avocado'] = 25
print('dict1 after Avocado insertion', dict1)