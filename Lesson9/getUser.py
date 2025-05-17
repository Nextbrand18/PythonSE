def welcome():
    # Prompt user for their name
        name = input("Please enter your name: ")
        xlen = len(name)

        # Check if the name is empty
        if not name:
            print("Name cannot be empty. Please enter your name.")
            welcome()

        elif xlen < 6:
            print("You have entered fewer character. Minimum character lenght is 6.")
            welcome()
        else:
            print (f"Hello {name} and welcome to the World of Games (WoG).\n" "Here you can find many cool games to play.")
            print ("\n")
        return name


def main():
    welcome()
               



if __name__ == '__main__':
    main() 