def find_discriminant(a, b, c):
    """
    PROTOTYPE:
        find_discriminant()
        Arguments -> (int) a, (int) b, (int) c
        Return values -> (int)
    DESCRIPTION:
        Takes three integer arguments representing coefficients of a quadratic equation and returns its discriminant.
    USAGE:
        discriminant(1, 1, 1) -> -3
        disriminant(1, -5, 6) -> 1
    ADDITIONALS:
        Discriminant of a quadratic equation = (Coefficient of x)^2 - 4 x (Coefficient of x^2) x (Constant term)
    """
    d = b**2 - 4*a*c
    return d


def find_nature(d):
    """
    PROTOTYPE:
        find_nature()
        Arguments -> (int) d
        Return values -> (str) nature
    DESCRIPTION:
        Takes discriminant of a quadratic as input and returns the nature of the equation.
    USAGE:
        nature(-3) -> "non-real (or complex)"
        nature(1) -> "real and unique"
        nature(0) -> "real and equal"
    ADDITIONALS:
        -> A quadratic equation always has two roots, which may either be real or complex.
        -> A quadratic equation has both of its root as real if it's d is greater than or equal to 0. Futhermore,
            -> if d is 0, then both the roots become equal
        -> A quadratic equation has complex roots if d is less than 0
    """
    if d > 0:
        nature = "real and unique"
    elif d == 0:
        nature = "real and equal"
    else:
        nature = "non-real (or complex)"
    return nature


def main():
    a = int(input("Coefficient of x^2: "))
    b = int(input("Coefficient of x: "))
    c = int(input("Constant term: "))
    discriminant = find_discriminant(a, b, c)
    nature = find_nature(discriminant)
    print("Nature of roots: Roots are " + nature)

# print(find_discriminant.__doc__)
# print(find_nature.__doc__)


if __name__ == "__main__":
    main()
