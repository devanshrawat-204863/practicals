def main():
    with open("intro.txt", "w") as file:
        inp = input("Enter a single line of text: ")
        file.write(inp)


if __name__ == "__main__":
    main()
