file_path = "Inputs/Day1-input.txt"
import re
def replace_spelled_out_numbers(input_string):
    # Check if the word is a spelled-out digit and replace it with its numerical value
    digit_mapping = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
                     'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

    # Split the input string into lines
    lines = input_string.split("\n")

    # Process each line
    for i, line in enumerate(lines):
        replaced_line = line.lower()  # Convert to lowercase for case-insensitive comparisons
        available_letters = set(replaced_line)

        for spelled_out in sorted(digit_mapping.keys(), key=len, reverse=True):
            # Replace only if the letters in the spelled-out digit are available
            if all(replaced_line.count(letter) >= spelled_out.count(letter) and letter in available_letters for letter in spelled_out):
                replaced_line = replaced_line.replace(spelled_out, digit_mapping[spelled_out])
                available_letters -= set(spelled_out)

        # Remove non-numeric characters
        lines[i] = ''.join(char for char in replaced_line if char.isdigit())

    # Join the lines back into a single string
    result_string = '\n'.join(lines)

    return result_string

# Example input string
input_string = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""

# Replace spelled-out numbers, remove non-numeric characters, and print the result
output_string = replace_spelled_out_numbers(input_string)
print(output_string)
