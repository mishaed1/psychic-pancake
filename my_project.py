import random
import json
import pyttsx3
import re
import time
import sys


def main():
    """This function executes the main logic of the program. The function calls other functions to display a
    welcome message, get a valid username, ask a question, generate an answer, and speak the answer to the user."""

    welcome_message()
    user_name = get_valid_name()
    ask_question()
    answer = shake_magic_8_ball(answers_file="custom_answers.json")
    speak_answer(answer, user_name)


def welcome_message():
    """This function prints a welcome message from the Magic 8-Ball program. It also tries to speak the welcome
    message using the `speak` function. If there is an `OSError`, it prints an error message and run without the
    sound."""

    print()
    print("*" * 70)
    try:
        print("\nWelcome to the Magic 8-Ball program!")
        speak("Welcome to the Magic 8-Ball program!")
    except OSError as e:
        print(f"Error initializing text-to-speech engine: {e}\n\nTHE GAME WILL CONTINUE WITHOUT THE SOUND.\n")
        print("=" * 70)
        return


def get_valid_name():
    """This function gets a valid username from the user. It loops until a valid name is entered."""

    while True:
        speak("What is your name?")
        name = input("\n... What is your name: ")

        if validate_name(name):
            print(f"\n... Hello, {name.title()}! Nice to meet you!")
            speak(f"Hello {name}! Nice to meet you!")
            speak("where are you from?")
            ask_place = input(f"\n... Where are you from?... ")

            speak(f"Oh... {ask_place} is a nice place!")
            print(f"\n... Oh, {ask_place.title()} is a nice place!")

            return name, ask_place
        else:
            print(f"\n... {name} Doesn't look like a real name. Please try again.")
            speak(f"{name} Doesn't look like a real name. Please try again.")


def ask_question():
    """This function asks if the user wants to continue."""

    print(f"\n... Ask me anything you want, or just type 'q' to end the game.\n")
    speak(f"Ask me anything you want. or just type 'q' to end the game.")
    prompt = input("... ")
    if prompt == "q" or prompt == "Q":
        print(f"\nOk, Good-by than!")
        speak(f"Ok. Good-by than!\n")
        print("\nTHANK YOU FOR USING THE MAGICAL 8-BALL PROGRAM!\n")
        print("*" * 70)
        sys.exit()

    else:
        return prompt


def shake_magic_8_ball(answers_file="custom_answers.json"):
    """This function generates an answer. It reads the answers from a JSON file and checks for errors."""
    try:
        with open(answers_file, "r") as file:
            answers_data = json.load(file)
        answers = answers_data.get("answers", [])
        if not answers:
            raise ValueError("The 'answers' list is empty or not present in the JSON file.")
        return f"{random.choice(answers)}"
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {answers_file} does not exist.")
    except json.JSONDecodeError:
        raise ValueError(f"Error decoding JSON in {answers_file}.")


def speak_answer(answer, user_name):
    time.sleep(0.5)
    print(f"\nMy answer is:")
    speak(f"My answer is")
    print(f"\n... {answer}\n")
    speak(answer)

    while True:
        prompt2 = input("\n... Do you have another question? Typ Y/y for (yes) or N/n for (no).\n> ")
        if prompt2 == "n" or prompt2 == "N":
            print(f"\nOk. Good-by than!")
            print("\nTHANK YOU FOR USING THE MAGICAL 8-BALL PROGRAM!\n")
            print("*" * 70)
            speak(f"Ok. Good-by than. and thank you! for using the Magic 8-Ball program.")
            sys.exit()
        elif prompt2 == "y" or prompt2 == "Y":
            ask_question()
            answer = shake_magic_8_ball(answers_file="custom_answers.json")
            speak_answer(answer, user_name)
        else:
            print(f"\n... I didn't get that, come again.")
            speak("I didn't get that, come again.")


def validate_name(name):
    return bool(re.match("^[A-Za-z -]+$", name))


def speak(text):
    """This function uses pyttsx3 to speak the text passed as an argument."""
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except OSError:
        pass


if __name__ == "__main__":
    main()
