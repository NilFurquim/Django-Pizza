orders = []


def add_order(name, flavor):
    order = {}
    order['name'] = name
    order['flavor'] = flavor
    orders.append(order)

print (orders)

add_order('Mario', 'Margarita')
add_order('Luigi', 'Pepperoni')

print(orders)
