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
                    choice = int(input())
                    print("Enter 1 for yes")
                    print("Enter 2 for no")
                    print("Enter 0 to exit")
                    if choice == 1:
                        print("Enter the amount of beeps you receive")
                        choice = int(input())
                        if choice == 1:
                            print("Bios ROM or CMOS battery failure please replace and retest")
                        elif choice == 2:
                            print("RAM is faulty or not detected")
                        elif choice == 3:
                            print("The motherboard is faulty please replace")
                        elif choice == 4:
                            print("RAM is faulty or not detected")
                        elif choice == 5:
                            print("Bios ROM or CMOS battery failure please replace and retest")
                        elif choice == 6:
                            print("The graphics card is bad please replace")
                        elif choice == 7:
                            print("The processor is bad please replace")
                        elif choice == 0:
                            print("The motherboard is faulty please replace")
                        else:
                            break
                    elif choice == 2:
                        print("Did you add a new part?")
                        choice = int(input())
                        print("Enter 1 for yes")
                        print("Enter 2 for no")
                        print("Enter 0 to exit")
                        if choice == 1:
                            print("Remove the newly added part and retest")
                            break
                        elif choice == 2:
                            print("Do you hear the hard drive spin up")
                            print("Enter 1 for yes")
                            print("Enter 2 for no")
                            print("Enter 0 to exit")
                            choice = int(input())
                            if choice == 1:
                                
                            elif choice == 2:
                                print("The drive is defective please replace it")
                                break
                        elif choice == 0:
                            break
                    elif choice == 0:
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
                    print("Enter 1 for yes")
                    print("Enter 2 for no")
                    print("Enter 0 to exit")
                    choice = int(input())
                    if choice == 1:
                        print("How many beeps do you receive?")
                        choice = int(input())
                        if choice == 1:
                            print("Bios ROM or CMOS battery failure please replace and retest")
                        elif choice == 2:
                            print("RAM is faulty or not detected")
                        elif choice == 3:
                            print("The motherboard is faulty please replace")
                        elif choice == 4:
                            print("RAM is faulty or not detected")
                        elif choice == 5:
                            print("Bios ROM or CMOS battery failure please replace and retest")
                        elif choice == 6:
                            print("The graphics card is bad please replace")
                        elif choice == 7:
                            print("The processor is bad please replace")
                        elif choice == 0:
                            print("The motherboard is faulty please replace")
                        else:
                            break
                    elif choice == 2:
                        print("Did you add a new part?")
                        print("Enter 1 for yes")
                        print("Enter 2 for no")
                        print("Enter 0 to exit")
                        choice = int(input())
                        if choice == 1:
                            print("Remove the newly added part and retest")
                        elif choice == 2:
                            print()
                        elif choice == 0:
                            break
                    elif choice == 0:
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
