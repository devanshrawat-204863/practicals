def main():
    upper, lower, vowels, consonants = 0, 0, 0, 0
    with open("myFile.txt", "r") as file:
        text = file.read()
        for char in text:
            if char.isalpha():
                if char.isupper():
                    upper += 1
                else:
                    lower += 1
                if char in 'aeiouAEIOU':
                    vowels += 1
                else:
                    consonants += 1
    print(f"Uppercase characters: {upper}\nLowercase characters : {lower}\nVowels:  {vowels}\nConsonants {consonants}")


if __name__ == "__main__":
    main()
