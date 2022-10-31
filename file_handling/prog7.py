def read(fname):
    with open(fname, "r") as file:
        data = file.read()
    return data


def write(fname, data):
    with open(fname, "a") as file:
        file.write(data)


def main():
    data1 = read("myFile.txt")
    data2 = read("intro.txt")
    data = data1 + data2
    write("merge.txt", data)


if __name__ == "__main__":
    main()
