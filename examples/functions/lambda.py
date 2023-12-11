add = lambda a, b: print(a + b)

add(5,2)

(lambda a, b: print(a + b))(11,18)

def multiplier(n):
    return lambda a: a * n

doubled = multiplier(2)
tripled = multiplier(3)

print(doubled(4))
print(tripled(4))