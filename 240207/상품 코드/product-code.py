class ProductCode:
    def __init__(self, name, code):
        self.name = name
        self.code = code

name_i, code_i = input().split()

a = ProductCode(name_i, int(code_i))

print(f"product 50 is codetree")
print(f"prodcut {a.code} is {a.name}")