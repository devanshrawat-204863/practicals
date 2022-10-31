def main():
    lines = []
    with open("myFile.txt", "w") as file:
        for i in range(3):
            lines.append(input("Enter a line of text: ") + "\n")
        file.writelines(lines)


if __name__ == "__main__":
    main()
