import re
import sys

# Regex for number at start of string => ^[0-9]
# Regex for strings that have -No 1000- => No\s\d+\D*$
# Regex for whitespace before -No 1999- => \s(?=No\s\d+\D*$)
# Regex for last number => \s(?=(\d+(?=\D*$)))


def address_parser(string):
    # Remove commas
    str = string.replace(',', '')

    # Checks if string starts with a number, then returns street string and number string
    if re.match(r'^[0-9]', str):
        [nb, street] = re.split(r'\s', str, maxsplit=1)
        return street.strip(), nb.strip()

    # Checks if string has <No 0000>, then splits into street string and a number string that includes -No-
    NbRegex = re.compile(r'No\s\d+\D*$')
    if (NbRegex.search(str) != None):
        [street, nb] = re.split(
            r'\s(?=No\s\d+\D*$)', str, maxsplit=1)
        return street, nb

    # Splits the string based on the whitespace before the last number, then trims street and number strings
    address = re.split(r"\s(?=(\d+(?=\D*$)))", str, maxsplit=1)
    street = address[0].strip()
    number = address[-1].strip()
    return street, number


if "__name__" == "__main__":
    print(sys.argv[0])
    t = 'Miritiba 339'
    e = 'Babaçu 500'
    s = 'Cambuí 804B'
    te = '4, Rue de la République'

    print(address_parser(t), address_parser(e),
          address_parser(s), address_parser(te))

    teste1 = 'Calle 44 No 1991'
    teste = '1002 Street'
    teste2 = 'Calle Sagasta, , , , 26'
    print(address_parser(teste1))
    print(address_parser(teste2))
    print(address_parser(teste))

    print(sys.argv[0])
    print(sys.argv[1])
    print(sys.argv[2])
