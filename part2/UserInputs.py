""" Quick introduction on how to get user inputs from the console """


""" Echo what the user says """


def echo():
    what_the_user_said = raw_input("Please input some text:\n")
    print ("You just said: " + what_the_user_said)


# echo()


""" The user enters text: if you want some integers, you have to transform it """


def double():
    value = int(raw_input("Enter a number:\n"))
    print (value * value)


# double()


""" A function that likes to chat with you, and never contradicts you """


def chat_with_me():
    print ("Speak with me as you like! (type `bored` if you want to stop)")
    while True:
        you_said = raw_input("Tell me more:\n")
        if "bored" in you_said:
            print ("Ok, let us stop there")
            break
        print ("I fully agree with you!")


# chat_with_me()
