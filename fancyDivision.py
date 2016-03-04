#Author: Jared Lefkort
#Date: 2/4/2016

dividend = int(input("Enter a dividend. "))

divisor = int(input("Enter a divisor. "))
#These are the inputs


if dividend%divisor == 0:
	print("{} divided by {} is ".format(dividend, divisor) + str(dividend/divisor))

	#this if statement will work for the exact multiples

else:
	print("{} divided by {} is ".format(dividend, divisor) + str(dividend//divisor) + " with a remainder of " + str(dividend%divisor))

	#this statement will work when their is a remainder

