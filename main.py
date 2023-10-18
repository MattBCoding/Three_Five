"""
Write a program that prints the numbers from 1 to 100.
But for multiples of three print "Three" instead of the number
and for the multiples of five print "Five".
For numbers which are multiples of both three and five print "ThreeFive".
"""


def three_five():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("ThreeFive")
        elif i % 3 == 0:
            print("Three")
        elif i % 5 == 0:
            print("Five")
        else:
            print(i)


if __name__ == "__main__":
    three_five()
