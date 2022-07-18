str_1 = input("Enter the first string: ")
# remove space and letters to upper case
print(''.join(sorted(list(str_1.upper().replace(' ', '')))))
