def prefix(name, gender):
    """
        PROTOTYPE:
            prefix()
            Arguments -> (str) name, (str) gender
            Return values -> (str)
        DESCRIPTION:
            Takes two string type arguments, name and gender.
            Adds an appropriate prefix to the name based on the value of gender and returns the same.
        USAGE:
            prefix("John", "M") -> "Mr John"
            prefix("Sarah", "F") -> "Ms Sarah"
            prefix("Blake") -> "Blake"
    """
    if gender == "M":
        pfix = "Mr"
    elif gender == "F":
        pfix = "Ms"
    else:
        return name
    return pfix + " " + name


def main():
    user_fname = input("First name: ")
    user_gender = input("Gender (M/F): ")
    prefixed_name = prefix(user_fname, user_gender)
    print("Welcome, " + prefixed_name)

# print(prefix.__doc__)


if __name__ == "__main__":
    main()
