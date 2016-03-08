#Author: Jared Lefkort
#Date: 2/4/2016

askAgain = "y"


while askAgain == "y":

	dividend = int(input("Enter a dividend. "))

	divisor = int(input("Enter a divisor. "))
	#These are the inputs

	quotient = dividend // divisor

	remainder = dividend % divisor 
	
	if remainder == 0:
		print("{} divided by {} is ".format(dividend, divisor) + str(quotient))
		askAgain = input("Would you like to go again? (y/n): ")

		#this if statement will work for the exact multiples

	else:
		print("{} divided by {} is ".format(dividend, divisor) + str(quotient) + " with a remainder of " + str(remainder))
		askAgain = input("Would you like to go again? (y/n): ")

		#this statement will work when their is a remainder

