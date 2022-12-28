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


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Invalid number of arguments')
        print('')
        print('Using Test Case:')
        print('Address: Palmeiras 12')
        ad = address_parser('Palmeiras 12')
        print('Street: ' + ad[0] + ' Number: ' + ad[1])
        print('')
    else:
        print('Address: ' + sys.argv[1])
        ad = address_parser(sys.argv[1])
        print('Street: ' + ad[0] + ' Number: ' + ad[1])
