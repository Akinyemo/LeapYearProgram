#Checks if the inputted String is a integer
def is_int(num):
	checker_is_int = 0
	for x in range(len(num)):
		if ord(num[x])>=48 and ord(num[x])<=57:
			checker_is_int+=1
	if checker_is_int == len(num):
		return True
	else:
		return False

def main():
    while True :
        try:
    	    userinput = input("Please enter year to be checked: ")
        except NameError:
            print("Incorrect Input")
        else:
            break

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
