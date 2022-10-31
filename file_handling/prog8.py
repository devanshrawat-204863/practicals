def main():
    upper, lower, digits = 0, 0, 0
    with open("merge.txt", "r") as file:
        text = file.read()
        for char in text:
            if char.isalpha():
                if char.isupper():
                    upper += 1
                else:
                    lower += 1
            elif char.isdigit():
                digits += 1
    print(f"Uppercase characters: {upper}\nLowercase characters : {lower}\nDigits: {digits}")


if __name__ == "__main__":
    main()
