
""" Expressions """


print (1)
print ("string")


""" Primitive operations """


print (1 + 2)
print (2 * 4)
print (100.0 - 22.37)


""" Abstraction mechanisms: variables """


initial_amount = 100.00
article_cost = 22.37
remaining_amount = initial_amount - article_cost
print (remaining_amount)


""" Primitive constructions: loops """


article_costs = [32.69, 19.99]
for cost in article_costs:
    remaining_amount = remaining_amount - cost


""" Abstraction mechanism: functions """


def get_remaining_amount(initial_qty, costs):
    final_qty = initial_qty
    for c in costs:
        final_qty = final_qty - c
    return final_qty

print (get_remaining_amount(200.0, [12.99, 32.99, 22.37]))


""" Recursive functions """


def get_remaining_amount_rec(initial_qty, costs):
    if len(costs) == 0:
        return initial_qty
    else:
        return get_remaining_amount_rec(initial_qty - costs[0], costs[1:])

print (get_remaining_amount_rec(200.0, [12.99, 32.99, 22.37]))
