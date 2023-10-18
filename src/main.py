"""
Write a program that prints the numbers from 1 to 100.
But for multiples of three print "Three" instead of the number
and for the multiples of five print "Five".
For numbers which are multiples of both three and five print "ThreeFive".
"""


def three_five(num):
    if num % 3 == 0 and num % 5 == 0:
        return "ThreeFive"
    elif num % 3 == 0:
        return "Three"
    elif num % 5 == 0:
        return "Five"
    else:
        return num


def main():
    for i in range(1, 101):
        print(three_five(i))


if __name__ == "__main__":
    main()
