#### psychic-pancake
###### magic_208_ball by Mikhail (@mishaed)

#### Project Title
# Talking Magic 208-Ball toy

#### video URL: https://youtu.be/VlA_opYF4o8
#### GitHub URL: https://github.com/mishaed1
## Description

The Magic 208-Ball project is a simple Python program that simulates a Magic 8-Ball toy. The user can ask a question, and 
the program will randomly select a response from a list of pre-defined phrases. The selected phrase is then printed to 
the console and/or spoken aloud using text-to-speech.

The program utilizes the `pyttsx3` library for text-to-speech functionality and reads the list of phrases from a JSON 
file. If the text-to-speach function is not available the program will print the answers to the console without speaking 
the text. It also provides the option for the user to ask additional questions or exit the program.

`test_custom_answers.json` file is a temporary json file with a single answer ("maybe") for testing purposes.
It is created by the `test_shake_magic_8_ball()` function. It also tests the function with an invalid JSON format in 
the _answers_file_ by
creating an `invalid_answers.json` file with invalid JSON content.

## Features

Welcome message with optional text-to-speech.
User-friendly interaction to get a valid username and location.
Text-to-speech functionality for a more interactive experience.
Graceful exit option

## Usage

To run the Magic 8-Ball program, simply execute the `project.py` file using a Python interpreter. The program will 
prompt you to enter your name, and ask you where're you from, and ask a question. After providing the question, the 
program will generate a random answer and display it on the console.

You can continue asking questions by selecting 'Y/y' for 'yes' when prompted, or exit the program by selecting 'N/n' 
for 'no'.

## Installation

1. Clone the repository or download the source code files. git clone https://github.com/mishaed1/psychic-pancake.git
2. Install the required dependencies by running `pip install pyttsx3` in your terminal.
3. Run the `my_project.py` file using a Python interpreter. `cd my_project.py`


## Contributing

Contributions to the Magic 8 Ball project are welcome. If you find any issues or have suggestions for improvements, 
feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

Thank you for using the Magic 8-Ball Python program! May your questions be answered wisely.

