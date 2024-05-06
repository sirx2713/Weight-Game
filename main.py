import datetime

now = datetime.datetime.now()
date = now.strftime("%d-%m-%y %H:%M:%S")

convertor = 0.45
username_attempts = 1
password_attempts = 1

username = input("Create username: ")
if len(username) <= 4:
    print("Username is too short!")
    username1 = input("Create username: ")
    while username_attempts <= 1:
        if len(username1) <= 4:
            print("Username is too short!")
            username1 = input("Create username: ")
        username_attempts = username_attempts + 1
        print("Too many attempts, refresh the page!")
    if len(username1) > 4:
        password = input("Create user password: ")
        while password_attempts <= 1:
            if len(password) <= 5:
                print("Password is too short!")
                password1 = input("Create user password: ")
            password_attempts = password_attempts + 1
            print("Too many attempts, refresh the page!")
        if len(password) > 5:
            print(f'{username1} welcome to the Weight Convertor Game!!!')
            weight = input(f'{username1} enter your weight: ')
            option = input(f'{username1} is this in (L)bs or (K)g: ')
            if option.upper() == "L":
                mass = float(weight) * convertor
                print(f'{username1} you weigh {mass}kg')
                print(f'{username1} completed the Weight Convertor Game on {date}')
            elif option.upper() == "K":
                mass = float(weight) / convertor
                print(f'{username1} you weigh {mass} pounds')
                print(f'{username1} completed the Weight Convertor Game on {date}')
            else:
                print("Invalid option, try again!")
                weight = input(f'{username1} enter your weight: ')
                option = input(f'{username1} is this in (L)bs or (K)g: ')
                if option.upper() == "L":
                    mass = float(weight) * convertor
                    print(f'{username1} you weigh {mass}kg')
                    print(f'{username1} completed the Weight Convertor Game on {date}')
                elif option.upper() == "K":
                    mass = float(weight) / convertor
                    print(f'{username1} you weigh {mass} pounds')
                    print(f'{username1} completed the Weight Convertor Game on {date}')
                else:
                    print("Too many invalid inputs, try refreshing the page!")
        elif len(password) > 5:
            print(f'{username1} welcome to the Weight Convertor Game!!!')
            weight = input(f'{username1} enter your weight: ')
            option = input(f'{username1} is this in (L)bs or (K)g: ')
            if option.upper() == "L":
                mass = float(weight) * convertor
                print(f'{username1} you weigh {mass}kg')
                print(f'{username1} completed the Weight Convertor Game on {date}')
            elif option.upper() == "K":
                mass = float(weight) / convertor
                print(f'{username1} you weigh {mass} pounds')
                print(f'{username1} completed the Weight Convertor Game on {date}')
            else:
                print("Invalid option, try again!")
                weight = input(f'{username1} enter your weight: ')
                option = input(f'{username1} is this in (L)bs or (K)g: ')
                if option.upper() == "L":
                    mass = float(weight) * convertor
                    print(f'{username1} you weigh {mass}kg')
                    print(f'{username1} completed the Weight Convertor Game on {date}')
                elif option.upper() == "K":
                    mass = float(weight) / convertor
                    print(f'{username1} you weigh {mass} pounds')
                    print(f'{username1} completed the Weight Convertor Game on {date}')
                else:
                    print("Too many invalid inputs, try refreshing the page!")
elif len(username) > 4:
    password = input("Create user password: ")
    while password_attempts <= 1:
        if len(password) <= 5:
            print("Password is too short!")
            password = input("Create user password: ")
        password_attempts = password_attempts + 1
        print("Too many attempts, refresh the page!")
    if len(password) > 5:
        print(f'{username} welcome to the Weight Convertor Game!!!')
        weight = input(f'{username} enter your weight: ')
        option = input(f'{username} is this in (L)bs or (K)g: ')
        if option.upper() == "L":
            mass = float(weight) * convertor
            print(f'{username} you weigh {mass}kg')
            print(f'{username} completed the Weight Convertor Game on {date}')
        elif option.upper() == "K":
            mass = float(weight) / convertor
            print(f'{username} you weigh {mass} pounds')
            print(f'{username} completed the Weight Convertor Game on {date}')
        else:
            print("Invalid option, try again!")
            weight = input(f'{username} enter your weight: ')
            option = input(f'{username} is this in (L)bs or (K)g: ')
            if option.upper() == "L":
                mass = float(weight) * convertor
                print(f'{username} you weigh {mass}kg')
                print(f'{username} completed the Weight Convertor Game on {date}')
            elif option.upper() == "K":
                mass = float(weight) / convertor
                print(f'{username} you weigh {mass} pounds')
                print(f'{username} completed the Weight Convertor Game on {date}')
            else:
                print("Too many invalid inputs, try refreshing the page!")
    elif len(password) > 5:
        print(f'{username} welcome to the Weight Convertor Game!!!')
        weight = input(f'{username} enter your weight: ')
        option = input(f'{username} is this in (L)bs or (K)g: ')
        if option.upper() == "L":
            mass = float(weight) * convertor
            print(f'{username} you weigh {mass}kg')
            print(f'{username} completed the Weight Convertor Game on {date}')
        elif option.upper() == "K":
            mass = float(weight) / convertor
            print(f'{username} you weigh {mass} pounds')
            print(f'{username} completed the Weight Convertor Game on {date}')
        else:
            print("Invalid option, try again!")
            weight = input(f'{username} enter your weight: ')
            option = input(f'{username} is this in (L)bs or (K)g: ')
            if option.upper() == "L":
                mass = float(weight) * convertor
                print(f'{username} you weigh {mass}kg')
                print(f'{username} completed the Weight Convertor Game on {date}')
            elif option.upper() == "K":
                mass = float(weight) / convertor
                print(f'{username} you weigh {mass} pounds')
                print(f'{username} completed the Weight Convertor Game on {date}')
            else:
                print("Too many invalid inputs, try refreshing the page!")
