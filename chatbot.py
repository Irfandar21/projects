import random

# Define a dictionary of responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm good, thanks!", "I'm doing well.", "I'm just a computer program, so I don't have feelings."],
    "what's your name": ["I'm a chatbot.", "I don't have a name, but you can call me ChatBot."],
    "bye": ["Goodbye!", "See you later!", "Farewell!"],
}

# Function to get a response based on user input
def get_response(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Check if the user input matches any predefined responses
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])

    # If no match is found, provide a default response
    return "what are you talking."

# Main loop to run the chatbot
print("ChatBot: Hello! How can I help you today?")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("ChatBot: Goodbye!")
        break
    response = get_response(user_input)
    print("ChatBot:", response)
