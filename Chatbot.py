import pyttsx3


def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.setProperty("volume", 0.8)
    engine.say(text)
    engine.runAndWait()


def get_user_input():
    user_input = input("You: ")
    return user_input


def main():
    print("Chatbot: Hello! How can I assist you today?")
    speak("Hello! How can I assist you today?")

    while True:
        user_input = get_user_input()

        if user_input.lower() == 'exit':
            break


        if "hello" in user_input.lower():
            print("Chatbot: Hello there!")
            speak("Hello there!")
        elif "how are you" in user_input.lower():
            print("Chatbot: I'm good, thank you! How about you?")
            speak("I'm good, thank you! How about you?")
        elif "fine" in user_input.lower() or "good" in user_input.lower():
            print("Chatbot: That's great to hear!")
            speak("That's great to hear!")
        elif "tell me a joke" in user_input.lower():
            print("Chatbot: Why don't scientists trust atoms?")
            print("Chatbot: Because they make up everything!")
            speak("Why don't scientists trust atoms? Because they make up everything!")
        elif "what is your name" in user_input.lower():
            print("Chatbot: I am a chatbot created by devansh gupta ji. You can call me Chatbot!")

            speak("I am a chatbot created by devansh gupta ji. You can call me Chatbot!")
        else:
            print("Chatbot: Sorry, I didn't quite catch that.")
            speak("Sorry, I didn't quite catch that.")

    print("Chatbot: Goodbye!")
    speak("Goodbye!")


if __name__ == '__main__':
    main()

-----------------------------------------------------------------------------------------------------------------------------------------------------------------
