""" Introducing abstraction building blocks """


""" Functions without parameters """


def greet():
    print ("Hello my friend!")
    print ("How are you doing?")


""" Functions taking parameters """


def greet_all(number):
    while number > 0:
        greet()
        number = number - 1


""" Functions doing something useful """


def get_remaining_amount(initial_qty, costs):
    final_qty = initial_qty
    for c in costs:
        final_qty = final_qty - c
    return final_qty

print (get_remaining_amount(200.0, [12.99, 32.99, 22.37]))

