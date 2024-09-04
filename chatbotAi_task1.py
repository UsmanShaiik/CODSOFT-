def chatbot_response(user_input):
    responses = {
        "hey": "Hey there! How can I help you today?",
        "hi": "Hi! What can I do for you?",
        "hello": "Hello! How can I assist you today?",
        "what's up": "Not much! How about you?",
        "howdy": "Howdy! What's on your mind?",
        "yo": "Yo! What's going on?",
        "bye": "Bye! Take care!",
        "goodbye": "Goodbye! Have a great day!",
        "see you": "See you later! Stay safe!",
        "catch you later": "Catch you later! Take it easy!",
        "name": "I'm just a simple chatbot here to help you!",
        "who are you": "I'm your friendly chatbot, here to assist you!",
        "what's your name": "I don't have a name, but you can call me Chatbot!",
        "time": "I'm not sure of the exact time, but it's always a good time to learn something new!",
        "date": "I can't tell you the date, but it's definitely a good day!",
        "weather": "I don't have weather information right now, but you could check a weather app!",
        "temperature": "I'm not sure of the temperature, but it's important to stay comfy!",
        "help": "Sure! I'm here to help. You can ask me about the weather, time, or even just say hello.",
        "thanks": "You're welcome! Anything else I can help with?",
        "thank you": "No problem! I'm here whenever you need me.",
        "how are you": "I'm just a bunch of code, but I'm doing great! How about you?",
        "what can you do": "I can chat with you, answer simple questions, and hopefully make your day better!",
        "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
        "joke": "Here's one: Why did the scarecrow win an award? Because he was outstanding in his field!",
        "funny": "I'm glad you think so! Got any jokes for me?",
        "bored": "Let's find something fun to do! How about a quick chat?",
        "what's new": "Not much on my end, but I'm here to chat if you want!",
    }
    
    normalized_input = user_input.lower()

    for keyword in responses:
        if keyword in normalized_input:
            return responses[keyword]

    return "I'm not sure I understood that. Could you try asking in a different way?"

def main():
    print("Welcome to the Simple Chatbot! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Bot: Goodbye!")
            break
        print("Bot:", chatbot_response(user_input))

if __name__ == "__main__":
    main()
