# Задание 3.5

def input_number():
    while True:
        number = input("Enter number: ")
        try:
            number = float(number)
        except ValueError:
            pass
        else:
            return number


# Задание 3.6

def input_word():
    while True:
        word = input("Enter word: ")
        k = word.strip(" ")
        if k.isalpha():
            return word
            break
        else:
            pass



