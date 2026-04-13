def chatbot():
    print("🤖 Chatbot: Hello! Type 'bye' to exit.\n")
    while True:
        user = input("You: ").lower()
        if user == "hello" or user == "hi":
            print("🤖 Chatbot: Hi there!") 
        elif "how are you" in user:
            print("🤖 Chatbot: I'm fine! How about you?")
        elif "your name" in user:
            print("🤖 Chatbot: I am a simple chatbot.")
        elif "help" in user:
            print("🤖 Chatbot: I can chat with you. Try saying hello!")
        elif "bye" in user:
            print("🤖 Chatbot: Goodbye! 👋")
            break
        else:
            print("🤖 Chatbot: Sorry, I don't understand.")
chatbot()