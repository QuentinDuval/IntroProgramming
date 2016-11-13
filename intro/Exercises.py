
""" List of exercises to complete after Basics """


"""
Exercise 1.a: Return the sum of the values
"""


def sum_values(values):
    return 0


print (sum_values([50.0, 25.0, 75.0]))



"""
Exercise 1.b: Use `sum_values` to improve the code that compute the remaining amount below
"""


def get_remaining_amount(initial_qty, costs):
    final_qty = initial_qty
    for c in costs:
        final_qty = final_qty - c
    return final_qty


print (get_remaining_amount(200.0, [50.0, 25.0, 75.0]))


"""
Exercise 2: Return the average value of a set of values.
"""


def average_value(values):
    return 0


print (average_value([1.0, 5.0, 4.0, 2.0]))

