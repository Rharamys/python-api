nums = [0, 1, 2, 3, 4]
num = 10
str = "My new string"

print(bytearray(nums))
print(bytearray(num))
print(bytearray(str, "UTF-8"))

banums = bytearray(nums)
banums.extend([10, 11, 12])
print(banums)

bastr = bytearray(str, "utf-8")
bastr[7:] = bytearray('String was modified', "utf-8")
print(bastr)