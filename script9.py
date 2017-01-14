import random, string

vowels='aeiouy'
consonants='bcdfghjklmnpqrstvwxz'
letters=vowels+consonants

letter_input_1=input("What letter do you want? Enter 'v' for vowels, 'c' for consonants, 'l' for any letter: ")
letter_input_2=input("What letter do you want? Enter 'v' for vowels, 'c' for consonants, 'l' for any letter: ")
letter_input_3=input("What letter do you want? Enter 'v' for vowels, 'c' for consonants, 'l' for any letter: ")

#print(letter_input_1 + letter_input_2 + letter_input_3)

def generator():
    # get letter 1
    if letter_input_1 == 'v':
        letter1 = random.choice(vowels)
    elif letter_input_1 == 'c':
        letter1 = random.choice(consonants)
    elif letter_input_1 == 'l':
        letter1 = random.choice(letters)
    else:
        letter1 = letter_input_1

    # get letter 2
    if letter_input_2 == 'v':
        letter2 = random.choice(vowels)
    elif letter_input_2 == 'c':
        letter2 = random.choice(consonants)
    elif letter_input_2 == 'l':
        letter2 = random.choice(letters)
    else:
        letter2 = letter_input_2

    # get letter 3
    if letter_input_3 == 'v':
        letter3 = random.choice(vowels)
    elif letter_input_3 == 'c':
        letter3 = random.choice(consonants)
    elif letter_input_3 == 'l':
        letter3 = random.choice(letters)
    else:
        letter3 = letter_input_3

    name = letter1 + letter2 + letter3
    return(name)

for i in range(20):
    print(generator())
