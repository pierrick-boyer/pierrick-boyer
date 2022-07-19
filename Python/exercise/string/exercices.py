str_1 = input("Enter the first string: ")
# remove space and letters to upper case
print(''.join(sorted(list(str_1.upper().replace(' ', '')))))


# ----------------------------------------------------------------------------------------------------------------------


def search():
    word = input("Enter the word you wish to find: ").upper()
    strn = input("Enter the string you wish to search through: ").upper()

    start = 0

    if word.find(strn):
        start += strn.count(word)
        return start
    else:
        return False


# ----------------------------------------------------------------------------------------------------------------------

