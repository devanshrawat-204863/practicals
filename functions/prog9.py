import random


def math():
    while True:
        num1 = random.randint(0,9)
        num2 = random.randint(0,9)
        if int(input(f"{num1} + {num2} = ")) == num1 + num2:
            print("Correct")
        else:
            print("Incorrect")


def eng():
    # There are over a thousand 3 letter words in English, so only those starting with 'J' are added here
    words = "Aw Ax Ay Ba Be Bi Bo By De Do Ed Ef Eh El Em En Er Es Et Ex Fa Fe Go Ha He Hi Hm Ho Id If In Is It Jo Ka Ki La Li Lo Ma Me Mi Mm Mo Mu My Na Ne No Nu Od Oe Of Oh Oi Om On Op Or Os Ow Ox Oy Pa Pe Pi Qi Re Sh Si So Ta Ti To Uh Um Un Ut We Wo Xi Xu Ya Ye Yo Za Jug Jet Joy Jew Jab Jot Jig Jam Jar Jog Jay Jus Jee Job Jaw Jun Joe"

    while True:
        word = input("Enter a two or three letter word: ")
        if not 2 <= len(word) <= 3:
            print("Incorrect")
        else:
            if word.lower() in words.lower():
                print("Correct")


def main():
    print("-- MENU --")
    print("To practice addition, input 1")
    print("To practice words, input 2")
    while True:
        selection = int(input("Enter choice: "))
        if selection not in [1, 2]:
            continue
        elif selection == 1:
            math()
        else:
            eng()


if __name__ == "__main__":
    main()