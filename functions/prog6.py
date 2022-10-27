def calc(x, y):
    """
    PROTOTYPE:
        calc()
        Arguments -> (int) x, (int) y
        Return values -> (int) x, (int) y
    DESCRIPTION:
        Takes two integer arguments, x and y.
        Swaps the two values if x is less than y, and return both the numbers.
    USAGE:
        calc(1, 2) -> 2, 1
        calc(1, 1) -> 1, 1
        calc(2, 1) -> 2, 1
    """
    if x < y:
        x, y = y, x
    return x, y


def main():
    n1 = int(input("n1: "))
    n2 = int(input("n2: "))
    print(f"Before: n1 = {n1}, n2 = {n2}")

    n1, n2 = calc(n1, n2)
    print(f"After: n1 = {n1}, n2 = {n2}")


# print(calc.__doc__)


if __name__ == "__main__":
    main()
