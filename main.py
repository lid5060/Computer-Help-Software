# start of the programme to help debug issues with a dell computer
print("Welcome to the software!")
# code used from https://medium.com/@dghadge2002/building-a-command-line-menu-in-python-exploring-different-applications-f970a61e6412
# making the menu that the user will see
while True:
        print("Does the computer turn on?")
        print("Enter 1 for Yes")
        print("Enter 2 for No")
        print("Enter 0 to exit programme")
        choice = int(input())
        if choice == 1:
            print("Is anything displayed on the screen?")
            print("Enter 1 if anything is displayed")
            print("Enter 2 if nothing is displayed")
            print("Enter 0 to exit")
# this is the sub menu for if anything is displayed on the screen
            choice = int(input())
            if choice == 1:
                print("Working")
                break
            elif choice == 2:
                print("Not working")
                break
            elif choice == 0:
                break
# end of the sub menu for if anything is displayed on scren
        elif choice == 2:
            print("Is the power button working?")
            print("Enter 1 for yes")
            print("Enter 2 for no")
            print("Enter 0 to exit")
            choice = int(input())
            if choice == 1:
                print("Power button works")
                break
            elif choice == 2:
                print("The power button isn't working please replace it")
                break
            elif choice == 0:
                break
        elif choice == 0:
            print("Exit")
            break
        else:
            print("Invalid choice!")
            break
# end of the menu
