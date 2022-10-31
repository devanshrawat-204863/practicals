def main():
    count1, count2 = 0, 0
    with open("intro.txt", "r") as file:
        lines = file.read().split("\n")
        for line in lines:
            count1 += 1
            if line.startswith('A') or line.startswith('B') or line.startswith('C'):
                count2 += 1

    print("Total number of lines " + str(count1))
    print("Number of lines starting with 'A', 'B', or 'C': " + str(count2))


if __name__ == "__main__":
    main()
