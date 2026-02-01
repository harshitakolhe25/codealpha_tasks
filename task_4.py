print("Chatbot started..! type 'bye' to exit: ")

while True:
    user_input=input("Enter your message: ").lower()

    if user_input=="hello":
        print("Bot: Hi!")
    elif user_input=="how are you":
        print("Bot: I'm fine,thanks!")
    elif user_input=="bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry ,I don't understand.")