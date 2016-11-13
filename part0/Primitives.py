""" Primitives of our language """


""" Expressions """


print (1)
print ("string")


""" Primitive operations """


print (1 + 2)
print (2 * 4)
print (100.0 - 22.37)
print ("string"[0])


""" Abstraction mechanisms: variables """


initial_amount = 100.00
article_cost = 22.37
remaining_amount = initial_amount - article_cost
print (remaining_amount)


""" Primitive constructions: loops """


article_costs = [32.69, 19.99]
for cost in article_costs:
    remaining_amount = remaining_amount - cost

print (remaining_amount)


""" Primitive constructions: conditionals """


if remaining_amount > 0:
    print ("Still some money left: " + str(remaining_amount))
else:
    print ("You are broke!")
