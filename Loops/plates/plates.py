import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# check if the plate start with 2 letters
def starts_with_two_letter(s):
    return len(s) >=2 and s[:2].isalpha()

# maximum 6 char and 2 minimum
def has_valid_length(s):
    return 2 <= len(s) <= 6


# No numbers in the middle of the plate
def no_middle_numbers(s):
    i = 0
    while i < len(s) and s[i].isalpha():
        i += 1
    #Now 'i' is the index where numbers start
    if i < len(s):
        if s[i] == '0':
            return False
        return s[i:].isdigit()
    return True

# no periods, spaces or punctuation marks are allowed
def no_invalid_characters(s):
    for char in s:
        if char in string.whitespace or char in string.punctuation:
            return False
    return True
def is_valid(s):
    return(starts_with_two_letter(s) and
           has_valid_length(s) and
           no_middle_numbers(s) and
           no_invalid_characters(s))

main()
