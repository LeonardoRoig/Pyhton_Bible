known_users = ["Alice","Bob","Claire","Dan","Emma","Fred","Georgie","Harry"]

while True:
    print("Hi, My name is Travis")
    name = str(input("What's your name?: ")).strip().capitalize()
    if name in known_users:
        print("Hello {}, Wellcome!".format(name))
        remove = input("would you like to be removed from the system? (Y/N): ").strip().lower()
        if remove == "y":
            known_users.remove(name)
            print("Your name has been removed!")
        elif remove == "n":
            print("No problem, I didn't want you leave anyway!")
            
    else:
        print("Hmmm I don't think I have met you yet {}!".format(name))
        add_me = input("Would you like to added to the system (Y/N)?: ").strip().lower()
        if add_me == "y":
            known_users.append(name)
            print("Now I saved your name!")
        elif add_me == "n":
            print("No worries, see you arround!")