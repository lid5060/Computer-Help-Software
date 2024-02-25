# start of the programme to help debug issues with a dell computer
print("Welcome to the software!")
# code used from https://medium.com/@dghadge2002/building-a-command-line-menu-in-python-exploring-different-applications-f970a61e6412
# making the menu that the user will see
while True:
        print("Does the computer turn on?")
        print("Press 1 for Yes")
        print("Press 2 for No")
        print("Press 0 to exit programme\n")
        choice = int(input())
        if choice == 1:
            print("Is anything displayed on the screen?\n")
            print("Press 1 if anything is displayed")
            print("Press 2 if nothing is displayed\n")
            choice = int(input())
            if choice == 1:
                print("Working")
                break
            elif choice == 2:
                print("Not working")
                break
        elif choice == 2:
            print("No")
            break
        elif choice == 0:
            print("Exit")
            break
        else:
            print("Invalid choice!")
            break
# end of the menu
