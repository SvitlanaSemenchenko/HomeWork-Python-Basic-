import string
def generate_hashtag(input_str):
    words = input_str.split()
    filtered_words = [''.join(c for c in word if c not in string.punctuation) for word in words]
    capitalized_words = [word.capitalize() for word in filtered_words if word]
    hashtag = '#' + ''.join(capitalized_words)
    if len(hashtag) > 140:
        hashtag = hashtag[:140]
    return hashtag

# Examples from homework:
sample_input1 = 'Python Community'
result_hashtag = generate_hashtag(sample_input1)
print(result_hashtag)
sample_input2 = 'i like python community!'
result_hashtag = generate_hashtag(sample_input2)
print(result_hashtag)
sample_input3 = 'Should, I. subscribe? Yes!'
result_hashtag = generate_hashtag(sample_input3)
print(result_hashtag)

# Example for user:
user_input = input("Please enter a string: ")
result_hashtag = generate_hashtag(user_input)
print(result_hashtag)
