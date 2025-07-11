my_str = "The cat jumped the brown cow"
animal = my_str[4:7]
print('The animal is a %s' % animal)

# String Search program: Hangman

word = 'onomatopoeia'
num_guesses = 10

hidden_word = '-' * len(word)

guess = 1

while guess <= num_guesses and '-' in hidden_word:
    print(hidden_word)
    user_input = input('Enter a character (guess #%d): ' % guess)

    if len(user_input) == 1:
        # Count the number of times the character occurs in the word
        num_occurrences = word.count(user_input)

        # Replace the appropriate position(s) in hidden_word with the actual character.
        position = -1
        for occurrence in range(num_occurrences):
            position = word.find(user_input, position + 1)  # Find the position of the next occurrence
            hidden_word = hidden_word[:position] + user_input + hidden_word[
                                                                position + 1:]  # Rebuild the hidden word string

        guess += 1

if not '-' in hidden_word:
    print('Winner!', end=' ')
else:
    print('Loser!', end=' ')

print('The word was %s.' % word)

# String split and joining - Extracting area code
phone_number = '977-555-3221'
number_segments = phone_number.split('-')
area_code = number_segments[0]
print('Area code:', area_code)

print('The {1} in the {0}'.format('hat','cat'))