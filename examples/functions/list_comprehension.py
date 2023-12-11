fruits = ["banana", "apple", "avocado", "pineapple", "strawberry"]
filter = 'p'

def filter_list(list, filter):
    filtered_list = []
    for item in list:
        if filter in item:
            filtered_list.append(item)
    return filtered_list

print(filter_list(fruits, filter))

new_list = [x for x in fruits if filter in x]

print(new_list)


number_list = [1,2,3,4,5]
new_number_list = [x * 2 for x in number_list]
print(new_number_list)