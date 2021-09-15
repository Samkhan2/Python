class Pizza:
    def __init__(self, type, price, size):
        self.type = type
        self.price = price
        self.size = size


piz = Pizza("chicken tikka", 23.5, "Medium")
print("Type : ", piz.type)
print("Price : ", piz.price)
print("Size : ", piz.size)



