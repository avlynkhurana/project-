contacts = [
    {
        "name":"John",
        "phone":"98765 56789",
        "conversation":[
                         "hi",
                         "Hello",
                         "I am good",
                         "How's your day"
                        ]
    },
    {
        "name": "Fionna",
        "phone": "98778 56798",
        "conversation": [
            "hello"
            "Hola"
            "I am not good"
            "How are you"
        ]
    },
    {
        "name": "George",
        "phone": "97687 45687",
        "conversation": [
            "hola",
            "bye",
            "lets play",
            "How are you doing"
        ]
    }
]
search_keyword = input("Enter keyword to search...")
print("search_keyword:",search_keyword)

for contact in contacts:
    #if contact["name"].lower().startswith(search_keyword.lower()):
    #if contact["name"].lower().__contains__(search_keyword.lower()):
     if contact["name"].lower().find(search_keyword.lower())>=0\
         or contact ["phone"].find(search_keyword)>=0:
         print(contact)
         print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
