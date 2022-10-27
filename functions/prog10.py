def login(uid, pwd):
    """
    PROTOTYPE:
        login()
        Arguments -> (str) uid, (str) pwd
        Return values -> None
    DESCRIPTION:
        Authenticate a user based on the whether username and password entered are genuine or not.
    """
    tries = 1
    username = "ADMIN"
    password = "St0rE@1"
    while tries < 3:
        if uid == username and pwd == password:
            print("login successful")
            return
        else:
            uid = input("username: ")
            pwd = input("password: ")
            tries += 1
    if tries >= 3:
        print("account blocked")


def main():
    uid = input("username: ")
    pwd = input("password: ")
    login(uid, pwd)


if __name__ == "__main__":
    main()
