print("Welcome to Nivora!")
print("Your Friendly Student Assistant")
print("--------------------------------")

while True:
    user = input("You: ").lower()

    if user == "hi":
        print("Nivora: Hi! How are you today?")

    elif user == "good":
        print("Nivora: That's great to hear! What can I help you with?")

    elif user == "bad":
        print("Nivora: Sorry to hear that. Hope your day gets better soon!")

    elif user == "how are you":
        print("Nivora: I am doing well. Thanks for asking!")

    elif user == "what is your name":
        print("Nivora: My name is Nivora.")

    elif user == "who created you":
        print("Nivora: I was created by Nivetha using Python.")

    elif user == "what can you do":
        print("Nivora: I can chat with you and answer simple questions.")

    elif user == "python":
        print("Nivora: Python is a simple and powerful programming language.")

    elif user == "ai":
        print("Nivora: AI helps machines learn and make decisions.")

    elif user == "internship":
        print("Nivora: Internships help students gain practical experience.")

    elif user == "placement":
        print("Nivora: Placements help students start their careers.")

    elif user == "motivate me":
        print("Nivora: Believe in yourself. Every expert was once a beginner!")

    elif user == "tell me a quote":
        print("Nivora: Success is the sum of small efforts repeated every day.")

    elif user == "thank you":
        print("Nivora: You're welcome!")

    elif user == "bye":
        print("Nivora: bye! Have a wonderful day!")
        break

    else:
        print("Nivora: Sorry, I didn't understand that.")