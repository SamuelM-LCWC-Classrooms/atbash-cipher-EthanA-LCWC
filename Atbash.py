def atbash(word):
    new_word = ""
    for letter in word:
        letter = ord(letter)
        if letter < 65:
            letter = chr(letter)
            new_word += letter
        elif letter < 97:
            to_take = 90 - letter
            letter = 65 + to_take
            letter = chr(letter)
            new_word += letter
        elif letter < 123:
            to_take = 122 - letter
            letter = 97 + to_take
            letter = chr(letter)
            new_word += letter
        else:
            letter = chr(letter)
            new_word += letter
    return new_word
