def story_time():
    print("Story time! It is 7am and your alarm goes off")
    option_one = str(input("Do you you hit the snooze alarm? [enter 'yes' or 'no']: "))
    if (option_one == "yes"):
        print("You have chosen to hit the snooze!")
    if (option_one == "no"):
        print("You have chosen not to hit the snooze alarm!")
        option_two= str(input("You need to get ready for school, do you get out of bed? [enter 'yes' or 'no']: "))
        if (option_two == "yes"):
            print("Sweet, you get ready to go to school and get there on time!")
        if (option_two == "no"):
            print("Oh no, you overslept and you wake up at 7:45am, no time to shower, just put on that sweater and we run to school")
    print("Story time is over!")
