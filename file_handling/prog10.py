def main():
    with open("merge.txt", "r") as file:
        target = input("Enter search term: ")
        count = 0
        text = file.read()
        words = text.split(' ')
        for word in words:
            if word == target:
                count += 1

        print(target + " appeared " + str(count) + " times in the file.")


if __name__ == "__main__":
    main()
