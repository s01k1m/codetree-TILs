class Code:
    def __init__(self, code, color, second):
        self.color = color
        self.code = code
        self.second = second

a, b, c =input().split()
c= int(c)
code = Code(a, b, c)

print(f"code : {code.code}")
print(f"color : {code.color}")
print(f"second : {code.second}")