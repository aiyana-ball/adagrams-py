import random

DISTRIBUTION_OF_LETTERS = {
    "A": 9,
    "B": 2,
    "C": 2,
    "D": 4,
    "E": 12,
    "F": 2,
    "G": 3,
    "H": 2,
    "I": 9,
    "J": 1,
    "K": 1,
    "L": 4,
    "M": 2,
    "N": 6,
    "O": 8,
    "P": 2,
    "Q": 1,
    "R": 6,
    "S": 4,
    "T": 6,
    "U": 4,
    "V": 2,
    "W": 2,
    "X": 1,
    "Y": 2,
    "Z": 1,
}

SCORE_CHART = {
    "A": 1,
    "B": 3,
    "C": 3,
    "D": 2,
    "E": 1,
    "F": 4,
    "G": 2,
    "H": 4,
    "I": 1,
    "J": 8,
    "K": 5,
    "L": 1,
    "M": 3,
    "N": 1,
    "O": 1,
    "P": 3,
    "Q": 10,
    "R": 1,
    "S": 1,
    "T": 1,
    "U": 1,
    "V": 4,
    "W": 4,
    "X": 8,
    "Y": 4,
    "Z": 10,
}


def draw_letters():
    letters_drawn = []
    available_letters = []
    for letter, limit in DISTRIBUTION_OF_LETTERS.items():
        available_letters.append(letter)
    while len(letters_drawn) <= 9:
        letter_choice = random.choice(available_letters)
        letter_count = letters_drawn.count(letter_choice)
        if letter_count < DISTRIBUTION_OF_LETTERS[letter_choice]:
            letters_drawn.append(letter_choice)
    return letters_drawn


def uses_available_letters(word, letter_bank):
    word = word.upper()
    for letter in word:
        letter = letter.upper()
        frequency_in_word = word.count(letter)
        frequency_in_bank = letter_bank.count(letter)
        if frequency_in_bank < frequency_in_word:
            return False
    return True


def score_word(word):
    score_total = 0
    for letter in word:
        letter = letter.upper()
        letter_points = SCORE_CHART[letter]
        score_total += letter_points
    if len(word) >= 7:
        score_total += 8
    return score_total


def get_highest_word_score(word_list):
    highest_score = 0
    highest_word = ""
    for word in word_list:
        score = score_word(word)
        if score > highest_score:
            highest_score = score
            highest_word = word
        elif score == highest_score:
            if len(word) == len(highest_word):
                pass
            elif len(word) == 10:
                highest_word = word
            elif len(word) < len(highest_word) and len(highest_word) != 10:
                highest_word = word
    word_and_score = [highest_word, highest_score]
    return word_and_score
