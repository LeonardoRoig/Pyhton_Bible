from turtle import title


films = {
    "Finding Dory": [3,5],
    "Bourne": [18,5],
    "Tarzan": [15,5],
    "Ghost Busters": [12,5]
}

while True:
    choice = str(input("What would you like to watch?: ").strip().title())
    if choice in films:
        age = int(input("How old are you?: ").strip())
        if age >= films[choice][0]:
            num_seats = films[choice][1]
            if films[choice][1] > 0:
                print("Enjoy the film!")
                num_seats = films[choice][1] -1
            else:
                print("Sorry, we are sold out!")
        else:
            print("You are too young to see {}!".format(choice))
    else:
        print("We don't have that film!")