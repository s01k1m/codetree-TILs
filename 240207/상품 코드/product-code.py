class ProductCode:
    def __init__(self, name="codetree", code="50"):
        self.name = name
        self.code = code

name_i, code_i = input().split()
a = ProductCode()
b = ProductCode(name_i, int(code_i))


print(f"product {a.code} is {a.name}")
print(f"product {b.code} is {b.name}")