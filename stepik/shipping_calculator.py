# The online store carries out express delivery for its products at a price of 1,000 rubles for the first product and
# 120 rubles for each subsequent product.
# Write a function get_shipping_cost (quantity) that takes a natural number as an argument -
# the number of items in the order and returns the shipping cost.
def get_shipping_cost(quantity):
    return (120 * (quantity - 1)) + 1000 if quantity > 1 else 1000


n = int(input())
print(get_shipping_cost(n))
