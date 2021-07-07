# Refactoring practice. Initial idea came from Head First Learn to Code, p195.

# Idea: Setting default values for users as we generate their avatars:
"""
hair_color = input('What color is your hair [brown]? ')
if hair_color == '':
    hair_color = 'brown'
print('You chose', hair_color, 'hair.')

hair_length = input('What hair length: long, medium, short, none [short]? ')
if hair_length == '':
    hair_length = 'short'
print('You chose', hair_length, hair_color, 'hair.')

eye_color = input('What color eyes do you choose [hazel]? ')
if eye_color == '':
    eye_color = 'hazel'
print('You chose', eye_color, 'eyes.')

gender = input('What gender do you choose [nonbinary]? ')
if gender == '':
    gender = 'nonbinary'
print('You chose a', gender, 'gender.')

has_glasses = input('Do they have glasses [no]? ')
if has_glasses == '':
    has_glasses = 'no'
print('You chose', has_glasses, 'glasses.')

has_beard = input('Do they have a beard [no]? ')
if has_beard == '':
    has_beard = 'no'
print('They have', has_beard, 'beard.')
"""

"""Reworking the code: Refactoring"""
# Here's where we're going to start using the refactoring process to simplify this load of code.
# This get_attribute() prints the same data in 12 lines vs. 24 lines above. It's also more flexible.
def get_attribute(query, default):
    question = query + ' [' + default + ']? '
    answer = input(question)
    if answer == '':
        answer = default
    print(f'You chose {answer}.')
    return answer

hair_color = get_attribute('What hair color', 'brown')
hair_length = get_attribute('What hair length', 'short')
eye_color = get_attribute('What eye color', 'hazel')
gender = get_attribute('What gender', 'nonbinary')
glasses = get_attribute('Do they wear glasses', 'no')
beard = get_attribute('Do they have a beard', 'no')