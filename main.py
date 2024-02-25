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
                print("Does the computer boot everytime?")
                print("Enter 1 if the computer boots ever time")
                print("Enter 2 if the computer doesnt boot everytime")
                print("Enter 0 to exit")
                choice = int(input())
                if choice == 1:
                    print("Does the computer beep?")
                    break
                elif choice == 2:
                    print("Replace PSU and retest")
                elif choice == 0:
                    break
            elif choice == 2:
                print("Troubleshoot the monitor and graphics card")
                break
            elif choice == 0:
                break
# end of the sub menu for if anything is displayed on screen
# start of the sub menu for if the power button is working
        elif choice == 2:
            print("Is the power button working?")
            print("Enter 1 for yes")
            print("Enter 2 for no")
            print("Enter 0 to exit")
            choice = int(input())
            if choice == 1:
                print("Does the computer boot everytime?")
                print("Enter 1 for yes")
                print("Enter 2 for no")
                print("Enter 0 to exit")
                choice = int(input())
                if choice == 1:
                    print("Does the computer beep?")
                    break
                elif choice == 2:
                    print("Replace PSU and retest")
                elif choice == 0:
                    break
            elif choice == 2:
                print("The power button isn't working please replace it")
                break
            elif choice == 0:
                break
# end of the sub menu for if the power button is working
        elif choice == 0:
            print("Exit")
            break
        else:
            print("Invalid choice!")
            break
# end of the menu
