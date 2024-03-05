import my_project as p
import pytest


def main():
    test_validate_name()
    test_shake_magic_8_ball()


def test_validate_name():
    assert p.validate_name("Anna-Lee")
    assert p.validate_name("Anna-Lee")
    assert not p.validate_name("Anna@Lee")
    assert not p.validate_name("123")
    assert not p.validate_name("John123")


def test_shake_magic_8_ball():
    # Create a temporary custom_answers.json for testing
    with open("test_custom_answers.json", "w") as file:
        file.write('{"answers": ["maybe"]}')

    # Test with a valid question and answers file
    assert "maybe" in p.shake_magic_8_ball(answers_file="test_custom_answers.json")

    # Test with an invalid answers file
    with pytest.raises(FileNotFoundError):
        p.shake_magic_8_ball(answers_file="nonexistent_file.json")

    # Test with an invalid JSON format in the answers file
    with open("invalid_answers.json", "w") as file:
        file.write("Invalid JSON file")
    with pytest.raises(ValueError, match="Error decoding JSON in invalid_answers.json"):
        p.shake_magic_8_ball(answers_file="invalid_answers.json")


# Define a fixture to mock the input function
@pytest.fixture
def mock_input(monkeypatch):
    def mock_input_func(prompt):
        if "What is your name?" in prompt:
            return "Anna-Lee"
        elif "Where are you from?" in prompt:
            return "New York"
        return "Anna-Lee"  # Default return value

    monkeypatch.setattr('builtins.input', mock_input_func)


def test_get_valid_name_valid_input(mock_input, capsys):
    """Test the get_valid_name function with valid input.
Args:
    mock_input: A mock object for simulating user input.
    capsys: A fixture for capturing stdout and stderr."""
    name, ask_place = p.get_valid_name()
    assert name == "Anna-Lee"
    assert ask_place == "New York"
    captured = capsys.readouterr()
    assert "Hello, Anna-Lee! Nice to meet you!" in captured.out


if __name__ == "__main__":
    main()

