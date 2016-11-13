
""" List of exercises to complete after Basics """


"""
Exercise 1.a: Return the sum of the values
"""


def sum_values(values):
    return 0


"""
Exercise 1.b: Use `sum_values` to improve the code that compute the remaining amount below
"""


def get_remaining_amount(initial_qty, costs):
    final_qty = initial_qty
    for c in costs:
        final_qty = final_qty - c
    return final_qty


"""
Exercise 2: Return the average value of a set of values.
"""


def average_value(values):
    return 0


"""
Exercise 3: Write a function `minimum` that finds the minimum value of a list.
Write a similar function to compute the `maximum` of a list of values.
"""


def minimum(values):
    return 0


def maximum(values):
    return 0


"""
Exercise 4: Write a function that displays a summary of the account information.

The arguments are:
- The first argument is the initial balance
- The second argument is a list of payment

The function should display (in order):
- The remaining amount
- The average payment value
- The maximum payment
- The minimal payment
- A line of 10 characters "-"
- The list of payments
"""


def display_summary(initial_balance, payments):
    print ("Initial amount: " + str(initial_balance))
    print ("Current amount: " + str(get_remaining_amount(initial_balance, payments)))
    print ("Minimal payment: " + str(minimum(payments)))
    print ("Maximal payment: " + str(maximum(payments)))
    print ("-" * 10)
    for payment in payments:
        print (payment)


display_summary(200.0, [12.99, 27.19, 49.99, 5.49])
