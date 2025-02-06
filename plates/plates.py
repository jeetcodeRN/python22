def main():
    plate = input("Plate: ")
    if is_valid(plate.upper()):  # Convert input to uppercase for case insensitivity
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    n = len(s)

    # Check length requirements
    if n < 2 or n > 6:
        return False

    # Check alphanumeric characters
    if not s.isalnum():
        return False

    # Check the first two characters are letters
    if not s[:2].isalpha():
        return False

    # Check if there are numbers in the middle
    if any(char.isdigit() for char in s[:-1]):
        return False

    # Separate characters and numbers
    chars = ''.join([char for char in s if char.isalpha()])
    numbers = ''.join([char for char in s if char.isdigit()])

    # Check if numbers are only at the end
    if numbers:
        # Check the first number is not '0' if plate length > 2
        if numbers[0] == '0' and n > 2:
            return False

    # If all checks pass, the plate is valid
    return True

if __name__ == "__main__":
    main()
