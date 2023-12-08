text1 = 'some text'
text2 = "another ' text"
text3 = '''another " text'''

print(text1)
print(text2)
print(text3)

# 'f' below stands for 'format'
print(f'Concat {text1} with {text2}')

# or
template = 'Concat {} with {}'
print(template.format(text1, text2))