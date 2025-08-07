# Simple Rule-Based Chatbot (CLI)

def chatbot():
    print("Hello! I'm ChatBot. Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ").lower()

        if user_input == 'exit':
            print("ChatBot: Goodbye! Have a great day.")
            break
        elif 'hello' in user_input or 'hi' in user_input:
            print("ChatBot: Hello! How can I help you today?")
        elif 'how are you' in user_input:
            print("ChatBot: I'm just a bunch of code, but I'm functioning perfectly!")
        elif 'what is your name' in user_input:
            print("ChatBot: I'm a simple Python chatbot.")
        elif 'help' in user_input:
            print("ChatBot: You can ask me basic questions like greetings or info about me.")
        else:
            print("ChatBot: Sorry, I don't understand that. Try something else!")

# Run the chatbot
if __name__ == '__main__':
    chatbot()
