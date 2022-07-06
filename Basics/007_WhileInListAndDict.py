def whileList():
    #
    #
    unconfirmed_users = ['pao','tablo','jafet']
    confirmed_users = []

    while unconfirmed_users:
        current_user = unconfirmed_users.pop()
        print(f"Verifying user >>> {current_user.title()}")
        confirmed_users.append(current_user)

    print(unconfirmed_users)
    print(confirmed_users)


    pets = ['cat','dog','dog','eagle','owl','tiger','mouse','dog']
    print(pets)
    while 'dog' in pets:
        pets.remove('dog')

    print(pets)

def whileDict():
    #We can use while to fill a dictionary with user Input
    responses = {}

    #set a flag to indicate that a poll is still active
    polling_active = True

    while polling_active:
        #Prompt for the persons name and response
        name = input("\nWhat is your name? ")
        response = input("\nWhat is your favorite programming language? ")
        #Store the responsenin the dictionary
        responses[name] = response

        repeat = input("Would you like to let anyone else to respond? (yes / no)  ")
        if repeat.lower() == "no":
            polling_active = False

        #when we have ended our poll we can print the results of responses
        print("--- Polling Results ---\n\n")
            print(f"{name} would like to learn {response}")
            for name, response in responses.items():


whileList()
whileDict()
