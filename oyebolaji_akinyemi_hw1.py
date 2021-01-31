#Main function of program
def main():
    userinput = input("Please enter year to be checked: ")
    if userinput % 4 == 0:
        if userinput % 100 == 0:
            if userinput % 400 == 0:
                print("This is a leap year")
            else:
                print("This is not a leap year")
        else:
            print("This is a leap year")
    else:
        print("This is not a leap year")        
           
main()