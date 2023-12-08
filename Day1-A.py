file_path = "Inputs/Day1-input.txt"

with open(file_path, "r") as file:
    input = file.read()


def extract_calibration_value(line):
    # Filter out non-numeric characters and get the first and last digits
    digits = [char for char in line if char.isdigit()]
    if len(digits) >= 2:
        first_digit = int(digits[0])
        last_digit = int(digits[-1])
    elif len(digits) == 1:
        first_digit = int(digits[0])
        last_digit = first_digit
    else:
        return 0  # Return 0 for lines with insufficient digits
    return first_digit * 10 + last_digit

def sum_calibration_values(calibration_document):
    # Split the calibration document into lines
    lines = calibration_document.split("\n")
    # Extract calibration values and calculate the sum
    total_sum = sum(extract_calibration_value(line) for line in lines if line)
    return total_sum

# Example calibration document
calibration_document = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

# Calculate and print the sum of calibration values
# Test - uncomment
#result = sum_calibration_values(calibration_document)

# Actual - uncomment
result = sum_calibration_values(input)

print("Day 1 - Part A: Sum of calibration values:", result)
# Answer is 54877