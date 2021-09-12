import sys

from converter import from_decimal, to_decimal


def main():
    number = sys.argv[1]
    convert_from_base = int(sys.argv[2])
    convert_to_base = int(sys.argv[3])

    if convert_from_base == 10:
        print(from_decimal(int(number), convert_to_base))
    else:
        number = to_decimal(number, convert_from_base)
        print(from_decimal(number, convert_to_base))


if __name__ == '__main__':
    main()
