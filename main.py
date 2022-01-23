# 🥸Basic principle

# item1 = "phone"
# item1_price = 100
# item1_quantity = 5
# item1_price_total = item1_price * item1_quantity


# print(item1)
# print(type(item1))  # str
# print(type(item1_price))  # int
# print(type(item1_quantity))  # int
# print(type(item1_price_total))  # int


# 🥸 Practice 1::
# class Item:
#     def calculate_total_price(self, i, j):
#         return i * j

#     def calculate_total_price2(self, x, y, z):
#         return x + y + z


# item1 = Item()
# item1.name = "cheap Phone"
# item1.price = 50
# item1.quantity = 5
# print(item1.calculate_total_price(item1.price, item1.quantity))


# item2 = Item()
# item2.name = "total_solditem_amount_for_today"
# item2.solditem1 = 1200
# item2.solditem2 = 600
# item2.solditem3 = 500
# print(item2.calculate_total_price2(item2.solditem1, item2.solditem2, item2.solditem3))


# # print(item1.name)
# # print(item2.name)


# =================================

# 🥸 Practice 2::


# class Item:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity


# item1 = Item("😭cheap Phone", 100, 5)
# item2 = Item("👩‍💻ipad", 2300, 3)

# print(item1.name)
# print(item1.price)
# print(item1.quantity)

# print(item2.name)
# print(item2.price)
# print(item2.quantity)


# # 🥸 Practice 3::
# class Item:
#     def __init__(self, name, price, quantity=0):  # quantity =0
#         self.name = name
#         self.price = price
#         self.quantity = quantity


# item1 = Item("😭cheap Phone", 100)
# item2 = Item("👩‍💻ipad", 2300)

# print(item1.name)
# print(item1.price)
# print(item1.quantity)

# print(item2.name)
# print(item2.price)
# print(item2.quantity)


# # 🥸 Practice 4::
# class Item:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def calculate_total_price(self):
#         return self.price * self.quantity


# item1 = Item("😭cheap Phone", 100, 3)
# item2 = Item("👩‍💻ipad", 2300, 3)

# print(item1.calculate_total_price())
# print(item2.calculate_total_price())


###BREAK TIME###
