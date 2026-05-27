# Q - Create a class caller Order which stores item & its price.
# Use Dunder function __gt__() to convey that:
    # order1 > order2 if order1's price is greater than order2's price.
    
class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
    
    def __gt__(self, other):
        return self.price > other.price
order1 = Order("Laptop", 1200)
order2 = Order("Smartphone", 800)
print(order1 > order2)