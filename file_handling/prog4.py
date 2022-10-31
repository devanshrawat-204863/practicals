def main():
    lst = []
    with open("myFile.txt", "r") as f:
        text = f.read()
        lines = text.split("\n")
        for line in lines:
            if 'a' in line:
                lst.append(line)
    with open("newFile.txt", "w") as newf:
        newf.writelines(lst)


if __name__ == "__main__":
    main()
