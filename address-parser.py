import re

# Regex for last number => \s(?=(\d+(?=\D*$)))
# Regex for number at start of string => ^[0-9]
# No\s\d+.*


def main(string):
    # Remove commas
    str = string.replace(',', '')

    # Checks if string starts with a number, then returns street string and number string
    if re.match(r'^[0-9]', str):
        [nb, street] = re.split(r'\s', str, maxsplit=1)
        return street.strip(), nb.strip()

    if re.match(r'No\s\d+\D*$', str):
        [street, nb] = re.split(
            r'\s(?=No\s\d+\D*$)', str, maxsplit=1)
        return street, nb

    # Splits the string based on the whitespace before the last number, then trims street and number strings
    address = re.split(r"\s(?=(\d+(?=\D*$)))", str, maxsplit=1)
    street = address[0].strip()
    number = address[-1].strip()
    return street, number


# t = 'Miritiba 339'
# e = 'Babaçu 500'
# s = 'Cambuí 804B'
# te = '4, Rue de la République'

# print(main(t), main(e), main(s), main(te))

teste1 = 'Calle 44 No 1991'
teste = '1002 Street'
teste2 = 'Calle Sagasta, , , , 26'
print(main(teste1))
print(main(teste2))
print(main(teste))

if "__name__" == "__main__":
    main(str)
