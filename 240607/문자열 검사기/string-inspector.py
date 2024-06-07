arr = list(input())
stack = []
flag = True
for char in arr:
    if char == "(" or char == "[":
        stack.append(char)

    if char == ")":
        if stack:
            last = stack.pop()
            if last != "(":
                flag = False
        else:
            flag = False
    elif char == "]":
        if stack:
            last = stack.pop()
            if last != "[":
                flag = False
        else:
            flag =false
if flag:
    print(1)
else:
    print(0)