#tmp1 = "CodeMobiles is the "best" traning center" --- is error
tmp1 = 'CodeMobiles is the "best" traning center' #fix it by use 'single quote'
print(tmp1)

#tmp1 = 'CodeMobiles's the "best" traning center' --- is error
tmp2 = 'CodeMobiles\'s the "best" traning center'  # fix it by use \back slash\
print(tmp2)

tmp = "CodeMobiles\'s the \"best\" traning center\nDo you believe?"  # fix it by use \back slash\
print(tmp)

# A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt)
