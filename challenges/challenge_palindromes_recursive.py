def is_palindrome_recursive(word, low_index, high_index):
    if len(word) <= 0 or type(word) != str:
        return False

    if low_index == high_index:
        inverted_word = word[::-1]
        if inverted_word == word:
            return True
        else:
            return False
    else:
        return is_palindrome_recursive(word, low_index + 1, high_index)
