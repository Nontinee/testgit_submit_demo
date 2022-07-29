# String
# tmp1 = "CodeMobiles"
tmp1 = 'CodeMobiles'
lenOfTmp1 = len(tmp1)

print(lenOfTmp1)
print(len(tmp1)) #It's the same value above

if tmp1 == "CodeMobiles":
    print(tmp1 + " is equal " + "CodeMobiles")
else:
    print(tmp1)

# if "CodeMobiles" == 'CodeMobiles':
#     print("yes")


x, y, z = 1, 2, 3
print("x is {},y is {},z is {}".format(x, y, z))

if "z" in "hey, what's up":
    print("there is hey")
else:
    print("No have hey")
