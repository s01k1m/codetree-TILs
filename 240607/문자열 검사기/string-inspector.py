arr = list(input())
stack = []
flag = True
for char in arr:
    if char == "(" or char == "[":
        stack.append(char)
        
    if char == ")":
        last = stack.pop()
        if last != "(":
            flag = False

    elif char == "]":
        last = stack.pop()
        if last != "[":
            flag = False

if flag:
    print(1)
else:
    print(0)