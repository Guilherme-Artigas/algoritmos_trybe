def alphabetical_order(word):
    organized_word = ""
    alphabet = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]

    for letter1 in alphabet:
        for letter2 in word:
            if letter1 == letter2:
                organized_word += letter2

    return organized_word


def compare_words(first_word, second_word):
    if len(first_word) <= 0 and len(second_word) <= 0:
        return False
    return first_word == second_word


def is_anagram(first_string, second_string):
    first_string_lower = str(first_string).lower()
    second_string_lower = str(second_string).lower()

    first_word_sorted = alphabetical_order(first_string_lower)
    second_word_sorted = alphabetical_order(second_string_lower)
    comparison = compare_words(first_word_sorted, second_word_sorted)

    result = (
        first_word_sorted,
        second_word_sorted,
        comparison
    )

    return result
