ALPHABET = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def from_decimal(num: int, base: int) -> str:
    """
        :param num: decimal integer that will be converted
        :param base: integer that represents base to which num will be converted
        :returns: num converted to numeral system with base as string
    """

    res = ''
    while num != 0:
        res += ALPHABET[num % base]
        num = int(num / base)
    return res[::-1]


def to_decimal(code: str, base: int) -> int:
    """
        :param code: string which is the number in some numeral system that will be
            converted to decimal integer
        :param base: integer that represents base of the numeral system of the code
        :returns: code converted to decimal integer
    """

    res = 0
    code = code[::-1]

    for i in range(len(code)):
        res += ALPHABET.index(code[i]) * base**i
    return res
