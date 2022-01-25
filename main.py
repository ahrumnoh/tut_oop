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


# # 🥸🥸 Practice 4::
# class Item:
# def __init__(self, name, price, quantity):
#     self.name = name
#     self.price = price
#     self.quantity = quantity

# def calculate_total_price(self):
#     return self.price * self.quantity


# Let's compare - part1
# item1 = Item("😭cheap Phone", 100, 3)
# item2 = Item("👩‍💻ipad", 2300, 3)

# #Let's compare - part1 & part2
# item1 = Item("😭cheap Phone", "100", 3)
# item2 = Item("👩‍💻ipad", "2300", 3)  #--> if you type integer with "", result will be  100100100 + 230023002300

# print(item1.calculate_total_price())
# print(item2.calculate_total_price())


###BREAK TIME###


# # 🥸🥸 Practice 4:: if you want to prevent the integer & Quantity, not to be negative


# class Item:

#     pay_rate = 0.8  # The pay rate after 20% discount

#     def __init__(self, name: str, price: float, quantity):
#         # Run validations to the received arguments
#         assert (
#             price >= 0
#         ), f"Price {price} is not greater than  or equal to zero!"  # what is f?
#         assert quantity >= 0, f"Price {price} is not greater than  or equal to zero!"

#         # Assign to self object
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def calculate_total_price(self):
#         return self.price * self.quantity


# Let's compare - part1
# item1 = Item(
#     "😭cheap Phone", 100, -3
# )  # if you put negative in quantity, AssertionError appeared
# item2 = Item(
#     "👩‍💻ipad", -2300, 3
# )  # if you put negative in price, AssertionError appeared

# item1 = Item("😭cheap Phone", 100, 3)  # only positive integer can be possible like this
# item2 = Item("👩‍💻ipad", 2300, 3)

# print(Item.__dict__)  # giving all the attricutes for class level
# print(item1.__dict__)  # giving all the attricutes for instance level


# # 🥸🥸 Practice 5::


class Item:

    pay_rate = 0.8  # The pay rate after 20% discount

    def __init__(self, name: str, price: float, quantity):
        # Run validations to the received arguments
        assert (
            price >= 0
        ), f"Price {price} is not greater than  or equal to zero!"  # what is f?
        assert quantity >= 0, f"Price {price} is not greater than  or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate


item1 = Item("😭cheap Phone", 100, 3)  # only positive integer can be possible like this
item1.apply_discount()
print(item1.price)

item2 = Item("Ipad2", 1000, 1)
item2.pay_rate = 0.8
item2.apply_discount()
print(item2.price)


item2 = Item("Ipad2", 1000, 1)  # same as item2 above, but different function
item2.apply_discount()
print(item2.price)


##BREAK TIME## 42:06
