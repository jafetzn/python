"""
Sometimes we will want to store multiple dictionaries in a list, or a list of itemsas a value in a dictionary. This is called nesting.
You can nest dictionaries inside a list, a list of items inside a dictionary, or even a dictionary inside a dictionary
"""

def peopleHobbies():
    #
    #
    print("<<Dictionaries inside a list>>\n")
    person1 = {"name":"jafet", "age":32, "sex":"male", "hobby":"fuck"}
    person2 = {"name":"tablo", "age":1, "sex":"male", "hobby":"sleep"}
    person3 = {"name":"santi", "age":8, "sex":"male", "hobby":"play"}
    person4 = {"name":"pao", "age":27, "sex":"feamale", "hobby":"fuck"}

    people = [person1, person2, person3, person4]

    for person in people:
        print(f"My name is {person['name']} , I'm {person['age']} years old and I like to {person['hobby']}")

    #We also want to store a list inside a dictionary, for example, using above dictionary on the hobby key, we can change that and update it to hobbies and put a list instead
    #of a single value
    print("\n<<A list inside a dictionary inside a list>>\n")

    person1 = {"name":"jafet", "age":32, "sex":"male", "hobbies":["fuck","play videogames","sleep","eat"]}
    person2 = {"name":"tablo", "age":1, "sex":"male", "hobbies":["sleep","get mad","laugh","smile"]}
    person3 = {"name":"santi", "age":8, "sex":"male", "hobbies":["play videogames","eat","watch tv"]}
    person4 = {"name":"pao", "age":27, "sex":"feamale", "hobbies":["fuck","read","dream","love"]}

    people = [person1, person2, person3, person4]

    for person in people:
        print(f"My name is {person['name']} , I'm {person['age']} years old and I like to {', '.join(person['hobbies'])}")

    # We can also nest a dictionary inside another dictionary but doing so it can complicate a little more our code instantly.
    # We will have a users list in which the username is the key and the value will be a dictionary that wil contain more information about the person
    #
    print("\keyInDictionary inside a dictionary\n")
    users = {
        "jafetzn":{
                "firstname":"Jafet",
                "lastname":"Zarate",
                "country":"Mexico",
                "email":"jafetzarate@outlook.com",
        },
        "poalita":{
                "firstname":"Paola",
                "lastname":"Martinez",
                "country":"Mexico",
                "email":"sweetlovely@gmail.com",
        },
        "tablito":{
                "firstname":"Pablo",
                "lastname":"Zarate",
                "country":"Mexico",
                "email":"tablito0110@live.com",
        }
    }

    print(f"{users}\n\n")

    for user, user_info in users.items():
        print(f"My name is {' '.join([user_info['firstname'],user_info['lastname']]).title()}, "
        + f"I'm from {user_info['country'].title()}, my tagname is {user}, "
        + f"and I registered using my email: {user_info['email']}")


peopleHobbies()
