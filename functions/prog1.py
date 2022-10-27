def divisible(x, y):
    """
        PROTOTYPE:
            divisible()
            Arguments -> (int) x, (int) y
            Return values -> (bool)
        DESCRIPTION:
            Takes a pair of integer values x and y and returns whether x is divisible by y.
        USAGE:
            divisible(1024, 8) will evaluate to True, whereas divisible(99, 5) will evaluate to False.
    """
    if x % y == 0:
        return True
    else:
        return False


def main():
    num = int(input("Enter a number: "))
    is_divisible = divisible(num, 7)
    if is_divisible:
        print(str(num) + " is divisible by 7.")
    else:
        print(str(num) + " is not divisible by 7.")


# print(divisible.__doc__)


if __name__ == "__main__":
    main()
