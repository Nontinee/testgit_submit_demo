tmp1 = 1
tmp1 = "Hey"
tmp1 = True

# print("Tmp1 = " + tmp1) tmp1 is booleen. It's not the same type btw before & after "+" then It's error
print(True + tmp1) # It's the same type then It's not error
print(tmp1 + tmp1)
print(False + True + tmp1)
print(True + True + tmp1)
print("Tmp1 = " + str(tmp1))
print(type(tmp1))

tmp1 = str(tmp1)
print("Tmp1 = " + tmp1)
# print("Tmp1 = " + str(tmp1)) tmp1 is string type then it's not need convert type to "str" but It's not error
print(type(tmp1))


tmp2 = 7
tmp2 = str(7)
print(bool(0))  # result is False in noly case "bool(0)"
print(bool(100)) #?
# print(bool(01)) #?
print(float("1234") + 1)
print(type(float("1234") + 1))
print("1234" + str(1))
print(str(float("1234")) + str(1)) # 1234.0 merge 1 equal 1234.01
