def main():
    with open("myFile.txt", "r") as f:
        data = f.read()
        words = data.split(" ")
        for word in words:
            print(word + "#", end="")

if __name__ == "__main__":
    main()
