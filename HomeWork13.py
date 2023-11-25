import string
def get_characters_between_letters(input_str):
    start_letter, end_letter = input_str.split('-')
    all_letters = string.ascii_letters
    result = all_letters[all_letters.index(start_letter):all_letters.index(end_letter) + 1]
    return result
user_input = input("Please enter two letters separated by a hyphen: ")
result = get_characters_between_letters(user_input)
print("Characters between the letters:", result)
